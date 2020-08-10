# Password Storage

Somewhat safe-ish storage for passwords
> it's better than writing it down in notes then sum1
> accidentally taking a peek at ur recommended food list
> then all of a sudden u have to either trust them or 
> change ur passwords both of which r bad

Dependancies: cryptography, pandas

## How to use

### Initialization
To initiate, save passwords in the *old.txt* document with 
the formatting below:

```
Location:Userid:Password
```
**!** Note that spaces *are* supported, you have been warnd

Then, ensure that both the existant *pass_file* and non-
existant *crypt_file* variables are filled before running 
the script.

* When using for the first time, the entered password will 
be saved as the key for accessing the encrypted file. 
**This cannot be changed** afterwards. To be able to use a 
new password, *crypt_file* must be assigned to a non-
existant file.

* After initialization, a new *crypt_file* will be generated 
in the *passwerds* directory. This will contain all the 
password information within, to allow the original 
*pass_file* to be deleted if so desired.

### Usage
Use the parameter `cat` to view all saved passwords

List of available commands
| Command | Input | Description|
| --- | --- | --- |
| `add` | `loc:userid:pass` | Adds the given values to the password cache
| `rm` | `index` | Removes the `index` row from the password cache
| `head` | `n` | Shows the first `n` rows of the password cache
| `tail` | `n` | Shows the final `n` rows of the password cache
| `sed`| `n` or `n1:n2` | Shows row `n` or range `n1:n2` of indexed passwords
| `cat` | *-None-* | Shows entire password cache
| `wq` | *-None-* | Save changes and quit
