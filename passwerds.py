###################################
#   Created by Robert Choi 2020   #
#  https://github.com/robert-choi #
###################################

from cryptography.fernet import Fernet, InvalidToken
from getpass import getpass
from os import path
import pandas as pd
from keygen import generate_key
from p_info import pass_file, crypt_file


def generate_crypt(fernet):
    """
    Generates encrypted file from text
    :param fernet: Fernet
    """
    with open(pass_file, 'rb') as infile:
        data = infile.read()
    crypt = fernet.encrypt(data)
    with open(crypt_file, 'wb') as ofile:
        ofile.write(crypt)
    print(f'Created new encrypted file {crypt_file}')


def edit_entries(data, command):
    """
    Edits the given dataframe according to input commands
    [add] -> adds the following entry to the dataframe
    [rm] -> removes the indexed entry from the dataframe
    :param data: DataFrame
    :param command: list
    :return: DataFrame
    """
    if len(command) !=2:
        print("Too many entries, I don't know what to do with this")
        return data
    elif command[0] == 'add':
        entry = command[1].split(':')
        if len(entry) !=3:
            print("Check your format, I can't add that")
            return data
        data = data.append(pd.Series(entry, index=data.columns), ignore_index=True)
        print(f"Added item {entry} to data")
        return data
    else:
        try:
            redex = int(command[1])
        except ValueError:
            print("I can't remove that index")
            return data
        if not redex in data.index:
            print("Index unavailable, use <cat> to check available indicies")
            return data
        removed = data.iloc[redex].values.tolist()
        data = data.drop(index=redex)
        print(f"Removed item {removed} from data")
        return data


def show_data(data, command):
    """
    Shows data from the given dataframe according to input commands
    [head] -> shows the first n lines of data
    [tail] -> shows the final n lines of data
    [sed] -> shows specific line n, or lines n1->n2
    :param data: DataFrame
    :param command: list
    """
    if len(command) !=2:
        print("Too many entries, I don't know what to do with this")
    elif command[0] in ('head', 'tail'):
        try:
            redex = int(command[1])
        except ValueError:
            print("I can't show that index")
            return
        if not redex in data.index:
            print("Index unavailable, use <cat> to check available indicies")
        elif command[0] == 'head':
            print(data.head(redex))
        else:
            print(data.tail(redex))
    else:
        redex = command[1].split(':')
        for i, num in enumerate(redex):
            try:
                redex[i] = int(num)
                if not int(num) in data.index:
                    print("Index unavailable, use <cat> to check available indicies")
                    raise ValueError
            except ValueError:
                print("I  can't show that index")
                return
        if len(redex) > 2:
            print("Too many indicies I don't know what to do with this")
        elif len(redex) == 1 or redex[0]==redex[1]:
            print(data.iloc[redex[0]:redex[0]+1,:])
        else:
            print(data.iloc[min(redex):max(redex),:])


def save_changes(data, fernet):
    """
    Re-writes crypt file with working version of dataframe
    :param data: DataFrame
    :param fernet: Fernet
    """
    str_converted = '\n'.join([':'.join(x) for x in data.values.tolist()])
    crypt = fernet.encrypt(str_converted.encode())
    with open(crypt_file, 'wb') as ofile:
        ofile.write(crypt)
    print('Changes saved')

###############################################################################

def main():
    password = getpass("Passwerd: ").encode()
    key = generate_key(password)
    f = Fernet(key)

    if not path.isfile(crypt_file):
        if not path.isfile(pass_file):
            print("Can't find either encrypted or text files")
            return
        generate_crypt(f)
    with open(crypt_file, 'rb') as infile:
        data = infile.read()
    try:
        read_data = str(f.decrypt(data).decode())
    except InvalidToken:
        print('Incorrekt passwerd')
        return

    d2list = [x.split(':') for x in read_data.split('\n')]
    pframe = pd.DataFrame(d2list, columns=['Location', 'Userid', 'Password'])
    
    running = True
    while running:
        try:
            cmd = input('Enter a command: ').split(' ')
            if cmd[0] in ('add', 'rm'):
                pframe = edit_entries(pframe, cmd)
            elif cmd[0] in ('head', 'sed', 'tail'):
                show_data(pframe, cmd)
            elif cmd[0] == 'cat':
                print(pframe)
            elif cmd[0] == 'wq':
                running = False
                save_changes(pframe, f)
                return
            else:
                print('Unknown command. List of known commands:\n'
                    '\tadd: Add item to data\n'
                    '\trm: Remove item by index\n'
                    '\thead: Show first n lines\n'
                    '\ttail: Show last n lines\n'
                    '\tsed: Show nth line(s)\n'
                    '\tcat: View working version\n'
                    '\twq: Save and quit\n'
                    'Or press CTRL+C to quit')

        except KeyboardInterrupt:
            running = False
            print('Exiting without saving...')

###############################################################################

if __name__ == '__main__':
    main()
