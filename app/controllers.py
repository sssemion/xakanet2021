from flask import render_template

from app import app
from app.forms.register import RegisterForm


@app.route("/", methods=["GET"])
def main():
    return render_template('main.html')


@app.route("/register",  methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template('login.html', form=form)
