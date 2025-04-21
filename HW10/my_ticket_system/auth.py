class Auth:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def login(self):
        self.username = input("Enter username:")
        self.password = input("Enter password:")

    def validate_user(self):
        with open("userpass.txt", "r") as f:
            for line in f:
                user, passw = line.strip().split("=")
                if user == self.username and passw == self.password:
                    print("login successful")
                    return True


admin = Auth()
admin.login()
