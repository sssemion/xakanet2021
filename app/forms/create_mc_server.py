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

    def __init__(self, *args, **kwargs):
        super(CreateMCServerForm, self).__init__(*args, **kwargs)
        default = "form-control"
        self.content = [self.name, self.host, self.rcon_port, self.rcon_password, self.nickname, self.make_active]
