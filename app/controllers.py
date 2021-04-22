from flask import render_template
from flask_login import current_user, logout_user
from werkzeug.utils import redirect

from app import app
from app.exceptions import InvalidLoginOrPassword, InsecurePassword, EmailAlreadyExists, UsernameAlreadyExists, \
    ServerAlreadyAdded, ServerConnectionError
from app.forms.create_mc_server import CreateMCServerForm
from app.forms.edit import EditForm
from app.forms.login import LoginForm
from app.forms.signup import SignUpForm
from app.forms.support import SupportForm
from app.services.mc_servers import create_server
from app.services.users import log_in, sign_up, get_user_json


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/signup", methods=["GET", "POST"])
def signup_page():
    if current_user.is_authenticated:
        return redirect("/")
    form = SignUpForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            form.password_again.errors.append("Пароли не совпадают")
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
    return render_template("user/signup.html", form=form)


@app.route("/edit")
def details():
    form = EditForm()
    return render_template("user/edit.html", form=form)


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
    return render_template("user/login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/server/new", methods=["GET", "POST"])
def create_server_page():
    if not current_user.is_authenticated:
        return redirect("/login")
    form = CreateMCServerForm()
    if form.validate_on_submit():
        try:
            create_server(form.name.data, form.host.data, form.rcon_port.data,
                          form.rcon_password.data, form.nickname.data, form.make_active.data)
            return redirect("/profile")
        except (ServerAlreadyAdded, ServerConnectionError) as e:
            form.host.errors.append(str(e))
    return render_template("create_mc_server.html", form=form)
 

@app.route("/profile/<string:username>")
def profile_page(username):
    user = get_user_json(username)
    return render_template("user/profile.html", user=user)


@app.route("/support")
def support():
    form = SupportForm()
    return render_template("support.html")
