# auth
from module_exceptions import UsernameAlreadyExists


class Authenticator:
    user_data = {}

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def user_add(self):
        if self.user not in Authenticator.user_data:
            Authenticator.user_data[self.user] = self.password
            print(f"{self.user} Added ")
        else:
            raise UsernameAlreadyExists(self.user, self.password)


aut = Authenticator("reza", "12345678")
aut.user_add()
aut = Authenticator("reza", "12345678")
aut.user_add()
