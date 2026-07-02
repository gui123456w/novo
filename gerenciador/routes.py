from gerenciador import app, database, bcrypt
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from gerenciador.forms import FormLogin, FormCriarConta, FormTarefa

from gerenciador.models import Usuario, Tarefa

from werkzeug.utils import secure_filename
import os
@app.route('/', methods=['GET', 'POST'])
def index():
    formlogin=FormLogin()

    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()

        if usuario and bcrypt.check_password_hash(usuario.password, formlogin.password.data):
            login_user(usuario, remember=True)
            return redirect(url_for('tarefas', id_usuario=usuario.id))


    return render_template('index.html', form=formlogin)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()

    if formcriarconta.validate_on_submit():
        password= bcrypt.generate_password_hash(formcriarconta.password.data)
        usuario = Usuario(
            email=formcriarconta.email.data,
            username=formcriarconta.username.data,
            password=password
        )

        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('tarefas', id_usuario=usuario.id))

    return render_template('criarconta.html', form=formcriarconta)

@app.route('/tarefas/<id_usuario>', methods=['GET', 'POST'])
@login_required
def tarefas(id_usuario):

    if int(id_usuario) == current_user.id:
        usuario = current_user
        form = FormTarefa()

        if form.validate_on_submit():
            arquivo = form.arquivo.data
            nome_seguro = secure_filename(arquivo.filename)

            caminho_projeto = os.path.abspath(os.path.dirname(__file__))
            caminho = os.path.join(
                caminho_projeto,
                app.config["UPLOAD_FOLDER"],
                nome_seguro
            )

            arquivo.save(caminho)

            tarefa = Tarefa(
                titulo=form.titulo.data,
                descricao=form.descricao.data,
                arquivo=nome_seguro,
                usuario_id=current_user.id
            )

            database.session.add(tarefa)
            database.session.commit()

            return redirect(url_for("tarefas", id_usuario=current_user.id))

        return render_template(
            "tarefas.html",
            usuario=usuario,
            form=form
        )

    else:
        usuario = Usuario.query.get_or_404(int(id_usuario))

        return render_template(
            "tarefas.html",
            usuario=usuario,
            form=None
        )

@app.route('/gerenciador')
@login_required
def gerenciador():
    tarefas = Tarefa.query.order_by(Tarefa.id.desc()).all()

    return render_template(
        "gerenciador.html",
        tarefas=tarefas
    )