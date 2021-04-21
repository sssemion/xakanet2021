from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    label = "username"
    login = StringField(label, validators=[DataRequired()], render_kw={
        "class": "form-control",
        "required": True,
        "placeholder": label
    })

    label = "password"
    password = StringField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "type": "password",
        "placeholder": label
    })
    submit = SubmitField("OK", render_kw={
        "class": "btn btn-primary",
        "type": "submit"
    })

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        default = "form-control"
        self.login.render_kw["class"] = default
        self.password.render_kw["class"] = default
        self.content = [self.login, self.password]
