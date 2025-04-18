# exceptions


class AuthException(Exception):

    def __init__(self, user=None, password=None):
        self.user = user
        self.password = None
        super().__init__(user, password)


class UsernameAlreadyExists(AuthException):
    def __init__(self, user):
        super().__init__(user=user)
        self.message = "this is user is already"
        super().__init__(self.message)


class PasswordTooShort(AuthException):
    def __init__(self, password):
        message = "Password is too short. It must be at least 8 characters."
        super().__init__(message)


class InvalidUsername(AuthException):

    def __init__(self, user):
        super().__init__(user=user)
        self.message = f"Invalid username: {user}"
        super().__init__(self.message)


class IncorrectPassword(AuthException):
    def __init__(self, password):
        super().__init__(password=password)
        self.message = "Incorrect  Password"
        super().__init__(self.message)
