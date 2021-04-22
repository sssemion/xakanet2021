from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class SupportForm(FlaskForm):
    label = "username"
    username = SelectField(label, validators=[DataRequired()], render_kw={
        "class": "form-control",
        "required": True,
        "placeholder": label
    })

    submit = SubmitField("OK", render_kw={
        "class": "btn btn-primary",
        "type": "submit"
    })
