from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    photo = FileField("Attach an image", render_kw={
        "class": "form-control-file btn btn-primary",
        "id": "photoField",
        "accept": ".jpg,.jpeg,.png"
    }, validators=[FileAllowed(["jpeg", "jpg", "png"], "Images only!")])

    label = 'link to twitch'
    twitch = StringField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "placeholder": label
    })

    label = 'link to youtube'
    youtube = StringField(label, validators=[DataRequired()], render_kw={
        "required": True,
        "placeholder": label
    })

    submit = SubmitField("OK", render_kw={
        "class": "btn btn-primary",
        "type": "submit"
    })

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        default = "form-control"
        self.photo.render_kw["class"] = "photo-item"
        self.twitch.render_kw["class"] = default
        self.youtube.render_kw["class"] = default
        self.content = [self.twitch, self.youtube]
