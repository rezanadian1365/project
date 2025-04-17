# exceptions


class AuthException(Exception):
    def __init__(self, user, password):
        super().__init__(self, user, password)


class UsernameAlreadyExists(AuthException):
    def __init__(self, user):
        super().__init__(user)
        print("this is user is already")


class PasswordTooShort(AuthException):
    def __init__(self, password):
        super().__init__(password)


class InvalidUsername(AuthException):
    pass
