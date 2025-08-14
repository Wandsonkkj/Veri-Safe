from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class MensagemForm(FlaskForm):
    titulo = StringField('newsTitle', validators=[DataRequired()])
    submit = SubmitField('🔍 Verificar se é Verdade')
