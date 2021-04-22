from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import URL


class EditForm(FlaskForm):
    photo = FileField("Attach an image", render_kw={
        "class": "form-control-file btn btn-primary",
        "id": "photoField",
        "accept": ".jpg,.jpeg,.png"
    }, validators=[FileAllowed(["jpeg", "jpg", "png"], "Images only!")])

    label = "Ссылка Twitch"
    twitch = StringField(label, validators=[URL()], render_kw={
        "placeholder": label
    })

    label = "Ссылка на YouTube"
    youtube = StringField(label, validators=[URL()], render_kw={
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
