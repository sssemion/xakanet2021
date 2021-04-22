from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class ChangePasswordForm(FlaskForm):
    label = "old password"
    old_password = PasswordField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "type": "password",
        "placeholder": label
    })
    label = "new password"
    new_password = PasswordField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "type": "password",
        "placeholder": label
    })

    label = "confirm password"
    confirm_password = PasswordField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "type": "password",
        "placeholder": label
    })

    submit = SubmitField("OK", render_kw={
        "class": "btn btn-primary",
        "type": "submit"
    })

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        default = "form-control"
        self.old_password.render_kw["class"] = default
        self.new_password.render_kw["class"] = default
        self.content = [self.old_password, self.new_password, self.confirm_password]
