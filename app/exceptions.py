class CustomException(Exception):
    pass


class EmailAlreadyExists(CustomException):
    def __init__(self, email):
        super(EmailAlreadyExists, self).__init__(f"Пользователь с email {email} уже зарегистрирован")


class UsernameAlreadyExists(CustomException):
    def __init__(self, username):
        super(UsernameAlreadyExists, self).__init__(f"Пользователь с именем {username} уже зарегистрирован")


class InvalidLoginOrPassword(CustomException):
    def __init__(self):
        super(InvalidLoginOrPassword, self).__init__("Неверный логин или пароль")


class InsecurePassword(CustomException):
    def __init__(self):
        super(InsecurePassword, self).__init__("Ненадежный пароль")
