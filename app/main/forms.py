from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired


class DisciplinaForm(FlaskForm):
    nome = StringField(
        'Cadastre a nova disciplina e o semestre associado:',
        validators=[DataRequired()]
    )
    semestre = RadioField(
        '',
        choices=[
            ('1º semestre', '1º semestre'),
            ('2º semestre', '2º semestre'),
            ('3º semestre', '3º semestre'),
            ('4º semestre', '4º semestre'),
            ('5º semestre', '5º semestre'),
            ('6º semestre', '6º semestre')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Cadastrar')