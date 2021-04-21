from flask import render_template
from flask_login import current_user, logout_user
from werkzeug.utils import redirect

from app import app
from app.exceptions import InvalidLoginOrPassword, InsecurePassword, EmailAlreadyExists, UsernameAlreadyExists
from app.forms.login import LoginForm
from app.forms.signup import SignUpForm
from app.services.users import log_in, sign_up


@app.route("/signup", methods=["GET", "POST"])
def signup_page():
    if current_user.is_authenticated:
        return redirect("/")
    form = SignUpForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            form.password_again.errors.append("Пароли не совпадают")
            print(1)
        else:
            try:
                sign_up(form.email.data, form.username.data, form.password.data)
                return redirect("/")
            except EmailAlreadyExists as e:
                form.email.errors.append(str(e))
            except UsernameAlreadyExists as e:
                form.email.errors.append(str(e))
            except InsecurePassword as e:
                form.password.errors.append(str(e))
    return render_template("signup.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        try:
            log_in(form.login.data, form.password.data, form.remember_me.data)
            return redirect("/")
        except InvalidLoginOrPassword as e:
            form.password.errors.append(str(e))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")