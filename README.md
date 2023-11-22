# passwordmanager

A python 3.12 password manager program. When ran, the user is prompted with a menu with 7 different options:
    
    (1) Generate a new key        
    (2) Load an exisiting key     
    (3) Create a new password file
    (4) Load exisiting password file
    (5) Add a new password
    (6) Get a password
    (q) Quit

### (1) Generate a new key
This creates a new key for the user to access their password file. The key is encrypted in base64. The user must specify the path they want the file to be created in. This can just be the file name and the file will be created where the program is located. Either this or option (2) is mandatory for opening the password files.

### (2) Load an existing key
This allows the user to access a password file using a key that has already been generated. The user must specify the path of the file to be read. This can just be the file name and the program will search for a file where the program is located. Either this or option (1) is mandatory for opening the password files.

### (3) Create a new password file
This creates a new file for passwords to be stored in. Passwords stored are encrypted using base64. The user must specify the path they want the file to be created in. This can just be the file name and the file will be created where the program is located.

### (4) Load exisitng password file
This uses a key that has been selected to open an exisitng password file. The user must specify the path of the file to be read. This can just be the file name and the program will search for a file where the program is located.

### (5) Add a new password
This allows a user to add a new password to the file that has been selected. The user must enter the site the password is for, e.g. "github", and then the password, e.g, "foobar". A password file and key must have both been loaded or generated for this to work.

### (6) Get a password
This allows a user to read a file from a password file. The user must enter the site the password is for, e.g. "github", and then the password, e.g, "foobar". A password file and key must have both been loaded or generated for this to work.

### (q) Quit
Quits the program.