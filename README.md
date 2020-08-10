# Password Storage
as the title states

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

Then, ensure that both the *pass_file* and *crypt_file* 
variables are filled before running the script.

When using for the first time, the entered password will 
be saved as the key for accessing the encrypted file. 
**This cannot be changed** afterwards. To be able to use a 
new password, *crypt_file* must be assigned to a non-
existant file.

### Usage
Use the parameter `cat` to view all saved passwords
