from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from gerenciador.models import Usuario

class FormLogin(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):

    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirmar_senha = PasswordField("Confirme Password", validators=[DataRequired(), EqualTo("password")])
    botao_confirmacao = SubmitField("Criar Password")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado, faça login novamente.")


class FormTarefa(FlaskForm):
    titulo = StringField(
        'Titulo', validators=[DataRequired()]
    )
    descricao = StringField('Descrição')

    arquivo = FileField(
        'Arquivo',
        validators=[
            FileAllowed(
                ['jpg', 'jpeg', 'png'],
                'Somente imagens!'
            )
        ]
    )

    botao_confirmacao = SubmitField('Salvar')