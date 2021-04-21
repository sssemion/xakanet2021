import flask_login

from app import login_manager
from app.data.db_session import create_session
from app.data.models.user import User
from app.exceptions import EmailAlreadyExists, UsernameAlreadyExists, InvalidLoginOrPassword, InsecurePassword


@login_manager.user_loader
def load_user(user_id):
    with create_session() as session:
        return session.query(User).get(int(user_id))


def sign_up(email, username, password):
    with create_session() as session:
        if session.query(User).filter(User.email == email).first() is not None:
            raise EmailAlreadyExists(email)
        if session.query(User).filter(User.username == username).first() is not None:
            raise UsernameAlreadyExists(username)
        if not is_password_secure(password):
            raise InsecurePassword
        user = User(email=email, username=username)
        user.set_password(password)
        session.add(user)
        session.commit()
        flask_login.login_user(user)


def log_in(login, password, remember_me=False):
    with create_session() as session:
        user = session.query(User).filter((User.email == login) | (User.username == login)).first()
        if user is None or not user.check_password(password):
            raise InvalidLoginOrPassword
        flask_login.login_user(user, remember=remember_me)
        return True


def is_password_secure(password: str) -> bool:
    return not (len(password) < 8 or
                password.isdigit() or
                password.isalpha() or
                password.islower() or
                password.isupper()) and password.isalnum()
