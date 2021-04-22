from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ConfirmEmailForm(FlaskForm):
    code = IntegerField("Код подтверждения из письма", validators=[DataRequired(), NumberRange(100000, 999999)])
    submit = SubmitField("Submit")
