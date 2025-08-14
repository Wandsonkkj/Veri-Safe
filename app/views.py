from flask import render_template
from main import app
from app.helpers import verificar_noticia
from app.models import MensagemForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homepage',methods=['POST','GET'])
def homepage():

    form = MensagemForm()
    resultado = ''

    if form.validate_on_submit():
        texto = form.titulo.data.strip() if form.titulo.data else ''
        print(texto)

        if texto:
            resultado = verificar_noticia(texto)
            print(resultado)


    return render_template('homepage.html',form=form,resultado=resultado or '')


