from gerenciador import app
from flask import render_template, url_for
from flask_login import login_required
from gerenciador.forms import FormLogin, FormCriarConta


@app.route('/', methods=['GET', 'POST'])
def index():
    formlogin=FormLogin()
    return render_template('index.html', form=formlogin)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formCriarConta=FormCriarConta()
    return render_template('criarConta.html', form=formCriarConta)

@app.route('/tarefas/<usuario>')
@login_required
def tarefas(usuario):
    return render_template('tarefas.html', usuario=usuario)


@app.route('/gerenciador', methods=['GET', 'POST'])
def gerenciador():
    return render_template('gerenciador.html')