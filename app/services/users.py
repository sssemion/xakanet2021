import datetime
import hashlib
import os
import random

import flask_login
from flask import render_template
from flask_login import current_user

from app import login_manager
from app.data.db_session import create_session, create_non_closing_session
from app.data.models.user import User
from app.exceptions import EmailAlreadyExists, UsernameAlreadyExists, InvalidLoginOrPassword, InsecurePassword, \
    ResourceNotFound, InvalidConfirmationCode
from app.services.email import send_email


@login_manager.user_loader
def load_user(user_id):
    with create_non_closing_session() as session:
        return session.query(User).get(int(user_id))


def sign_up(email, username, password, photo=None):
    with create_session() as session:
        if session.query(User).filter(User.email == email).first() is not None:
            raise EmailAlreadyExists(email)
        if session.query(User).filter(User.username == username).first() is not None:
            raise UsernameAlreadyExists(username)
        if not is_password_secure(password):
            raise InsecurePassword
        user = User(email=email, username=username)
        user.set_password(password)

        confirmation_code = random.randint(100000, 999999)
        user.confirmation_code = confirmation_code
        send_email("Подтверждение учетной записи Stream Support",
                   sender=os.environ.get("MAIL_USERNAME"),
                   recipients=[email],
                   text_body=render_template("email/confirmation.txt", confirmation_code=confirmation_code),
                   html_body=render_template("email/confirmation.html", confirmation_code=confirmation_code))

        session.add(user)
        session.commit()

        if photo:
            photo_filename = generate_photo_filename(user.id)
            photo.save(f"app/static/img/profile-photos/{photo_filename}.{photo.filename.split('.')[-1]}")
        flask_login.login_user(user)


def confirm_email(code):
    with create_session() as session:
        user = session.query(User).get(current_user.id)
        if user.confirmation_code != code:
            raise InvalidConfirmationCode
        user.confirmed = True
        user.confirmation_code = None


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


def get_user_json(username):
    with create_session() as session:
        user = session.query(User).filter(User.username == username).first()
        if user is None:
            raise ResourceNotFound
        if current_user.is_authenticated and user == current_user and current_user.confirmed:
            return user.to_dict(additional=["email", "active_mc_server", "mc_servers", "confirmed", "money"])
        return user.to_dict()


def generate_photo_filename(unique_id):
    user_id_hash = hashlib.md5(str(unique_id).encode("utf-8")).digest()
    datetime_hash = hashlib.md5(str(datetime.datetime.now()).encode("utf-8")).digest()
    return hashlib.sha1(user_id_hash + datetime_hash).hexdigest()
