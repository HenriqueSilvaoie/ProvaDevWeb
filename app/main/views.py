from datetime import datetime
from flask import render_template, redirect, url_for, flash
from . import main
from .forms import DisciplinaForm
from .. import db
from ..models import Disciplina

@main.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@main.route('/disciplinas', methods=['GET', 'POST'])
def disciplinas():
    form = DisciplinaForm()
    if form.validate_on_submit():
        disciplina_existente = Disciplina.query.filter_by(nome=form.nome.data).first()
        if disciplina_existente is None:
            nova_disciplina = Disciplina(
                nome=form.nome.data,
                semestre=form.semestre.data
            )
            db.session.add(nova_disciplina)
            db.session.commit()
        else:
            flash('Essa disciplina já está cadastrada!')
        return redirect(url_for('main.disciplinas'))

    lista_disciplinas = Disciplina.query.all()
    return render_template('disciplinas.html', form=form, disciplinas=lista_disciplinas)