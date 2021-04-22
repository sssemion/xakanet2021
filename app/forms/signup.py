from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class SignUpForm(FlaskForm):
    label = "username"
    username = StringField(label, validators=[DataRequired()], render_kw={
        "class": "form-control",
        "required": True,
        "placeholder": label
    })

    label = "email"
    email = StringField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "type": "email",
        "placeholder": label
    })

    label = "password"
    password = StringField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "type": "password",
        "placeholder": label
    })

    label = "confirm password"
    password_again = StringField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "type": "password",
        "placeholder": label
    })

    photo = FileField("Attach an image", render_kw={
        "class": "form-control-file btn btn-primary",
        "id": "photoField",
        "accept": ".jpg,.jpeg,.png"
    }, validators=[FileAllowed(["jpeg", "jpg", "png"], "Images only!")])

    submit = SubmitField("OK", render_kw={
        "class": "btn btn-primary",
        "type": "submit"
    })

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        default = "form-control"
        photo = "photo-item"
        self.email.render_kw["class"] = default
        self.username.render_kw["class"] = default
        self.password.render_kw["class"] = default
        self.password_again.render_kw["class"] = default
        self.photo.render_kw["class"] = photo
        self.content = [self.email, self.username, self.password, self.password_again]
