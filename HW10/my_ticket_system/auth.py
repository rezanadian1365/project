class Auth:
    """
    this class is used admin authentication
    read username and password from userpass.txt file
    check if the username and password are correct"""

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def login(self):
        self.username = input("Enter username:")
        self.password = input("Enter password:")

    def validate_user(self):

        user_pass = {}
        with open(
            "c:/Users/rezaNadian/Desktop/hw6/HW10/my_ticket_system/userpass.txt", "r"
        ) as f:
            for line in f:
                key, value = line.strip().split("=")
                user_pass[key] = value
        print(
            {
                key: (value if key != "password" else "*" * len(value))
                for key, value in user_pass.items()
            }
        )

        if (
            self.username == user_pass["username"]
            and self.password == user_pass["password"]
        ):
            print("login successful")
            return True
        else:
            print("login failed")
            return False
