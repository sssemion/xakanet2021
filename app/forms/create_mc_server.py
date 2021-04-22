from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, IPAddress


class CreateMCServerForm(FlaskForm):
    name = StringField("Имя сервера", validators=[DataRequired()])
    host = StringField("Host", validators=[IPAddress()])
    rcon_port = IntegerField("Rcon port", validators=[DataRequired()])
    rcon_password = PasswordField("Rcon password", validators=[DataRequired()])
    nickname = StringField("Ник на сервере", validators=[DataRequired()])
    make_active = BooleanField("Сделать активным")

    submit = SubmitField("Отправить")
