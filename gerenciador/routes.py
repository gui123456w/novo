from flask import Flask, render_template, url_for
from gerenciador import app
from flask_login import login_required


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gerenciador/<usuario>')
@login_required
def gerenciador(usuario):
    return render_template('gerenciador.html', usuario=usuario)


@app.route('/tarefa/')
def tarefa():
    return render_template('tarefas.html')