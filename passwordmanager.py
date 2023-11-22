from cryptography.fernet import Fernet

class passwordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
    def create_key(self,path):
        self.key = Fernet.generate_key()
        with open(path, "wb") as f:
            f.write(self.key)
    def load_key(self, path):
        with open(path, "rb") as f:
            self.key = f.read()
    def create_password_file(self, path, initial_values=None):
        self.password_file = path
        if initial_values is not None:
            for key, value in initial_values.items(): #.items can be used to iterate across tuples in a dictionary
                self.add_password(key, value)
    def load_password_file(self,path):
        self.password_file = path
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode
    def add_password(self, site, password):
        self.password_dict[site] = password
        if self.password_file is not None:
            with open(self.password_file, "a+") as f:
                encrypted =Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode()+ "\n")
    def get_password(self, site):
        return self.password_dict[site]

def main():
    password ={
        "email": "foobar",
        "instagram": "barfoo",
        "youtube": "foobarbaz",
        "foobar": "bleh"
        }
    pm = passwordManager()
    print("""What do you want to do?
    (1) Generate a new key
    (2) Load an exisiting key
    (3) Create a new password file
    (4) Load exisiting password file
    (5) Add a new password
    (6) Get a password
    (q) Quit
""")
    done = False
    while not done:
        choice = input("Enter your choice: ")
        match choice:
            case '':
                print()
                print("Please enter a command")
            case '1':
                print()
                path = input("Enter the path you want your key to be generated to: ")
                pm.create_key(path)
            case '2':
                print()
                path = input("Enter the path you want your key to be loaded from: ")
                pm.load_key(path)
            case '3':
                print()
                path = input("Enter the path you want your file to be created in: ")
                pm.create_password_file(path, password)
            case '4':
                print()
                path = input("Enter the path you want your file to be loaded from: ")
                pm.load_password_file(path)
                #test
            
            