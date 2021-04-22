from flask import render_template

from app import app
from app.forms.login import LoginForm
from app.forms.register import RegisterForm


@app.route("/", methods=["GET"])
def main():
    return render_template('main.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template('user/register.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('user/login.html', form=form)


@app.route("/profile/<string:username>", methods=["GET"])
def profile(username):
    return render_template('user/profile.html', user={"username": "me", "email": "my.open@mail.ru",
                                                      "links": [{"place": "youtube", "link": "https://youtube.com"},
                                                                {"place": "twitch", "link": "https://twitch.tv"}],
                                                      "servers": [{"name": "Germany", "id": 1}]})
