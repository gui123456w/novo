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

@app.route('/gerenciador/<usuario>')
@login_required
def gerenciador(usuario):
    formCriarConta = FormCriarConta()
    return render_template('gerenciador.html', usuario=usuario)


@app.route('/tarefa/')
def tarefa():
    return render_template('tarefas.html')