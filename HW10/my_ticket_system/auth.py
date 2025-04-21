class Auth:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def login(self):
        self.username = input("Enter username:")
        self.password = input("Enter password:")

    def validate_user(self):
        user_pass = {}
        with open("userpass.txt", "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                user_pass[user] = passw
        if (
            self.username == user_pass["username"]
            and self.password == user_pass["password"]
        ):
            print("login successful")
            return True
        else:
            print("login failed")
            return False


admin = Auth()
admin.login()
admin.validate_user()
