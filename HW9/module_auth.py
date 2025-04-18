# auth
from module_exceptions import (
    UsernameAlreadyExists,
    IncorrectPassword,
    PasswordTooShort,
    InvalidUsername,
)


class Authenticator:
    user_data = {}
    logged_users = set()

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def user_add(self):
        if len(self.password) < 8:
            raise PasswordTooShort(self.password)

        if self.user in Authenticator.user_data:
            raise UsernameAlreadyExists(self.user)

        Authenticator.user_data[self.user] = self.password
        print(f"{self.user} Added ")

    def login(self):
        if self.user not in Authenticator.user_data:
            raise InvalidUsername(self.user)

        if Authenticator.user_data[self.user] != self.password:
            raise IncorrectPassword()
        Authenticator.logged_users.add(self.user)

        print(f"{self.user} Logged in successfully!")

    def is_logged_on(self):
        return self.user in Authenticator.logged_users

    def log_out(self):

        if self.user in Authenticator.logged_users:
            Authenticator.logged_users.remove(self.user)
            print(f"{self.user} Logged out successfully!")
        else:
            print(f"{self.user} is not logged in.")


aut = Authenticator("Reza", "12345678")
aut.user_add()
aut.login()
print(aut.is_logged_on(), "user is login")
aut.log_out()
aut = Authenticator("Reza", "12345678")
aut.user_add()
