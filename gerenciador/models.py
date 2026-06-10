from gerenciador import database, login_manager
from datetime import datetime
from flask_login import UserMixin

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(250), nullable=False)
    email = database.Column(database.String(250), nullable=False)


    @login_manager.user_loader
    def load_usuario(id_usuario):
        return Usuario.query.get(int(id_usuario))

class Tarefa(database.Model):
    id_tarefa = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(250), nullable=False)
    descricao = database.Column(database.String(250), nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)

class Projeto(database.Model):
    id_projeto = database.Column(database.Integer, primary_key=True)
