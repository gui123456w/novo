from gerenciador import database, login_manager
from datetime import datetime
from flask_login import UserMixin

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    password = database.Column(database.String(250), nullable=False)
    username = database.Column(database.String(250), nullable=False)
    email = database.Column(database.String(250), nullable=False, unique=True)

    cargo = database.Column(database.String(50), nullable=False, default="funcionário")
    arquivo = database.relationship('Arquivo', backref='usuario', lazy=True)
    tarefas = database.relationship(
        'Tarefa',
        backref='usuario',
        lazy=True
    )
    @login_manager.user_loader
    def load_usuario(id_usuario):
        return Usuario.query.get(int(id_usuario))

class Tarefa(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String(250), nullable=False)
    descricao = database.Column(database.String(250), nullable=False)
    status = database.Column(database.String(250), default='Pendente')
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    arquivo = database.Column(database.String, default='default.png')

    concluida = database.Column(database.Boolean, default=False)
    usuario_id = (database.Column
                (database.Integer,
                database.ForeignKey('usuario.id'),
                nullable=False))

class Gerenciador(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(250), nullable=False)
    descricao = database.Column(database.String(250), nullable=False)
    status = database.Column(database.String(250), default='Em andamento')
    usuario_id = database.Column(
        database.Integer,
        database.ForeignKey('usuario.id'),
        nullable=False
    )

