# rotas do projeto
from app import App
from flask import render_template, url_for

@App.route('/')
def entrada():
    return render_template('index.html')

@App.route('/homepage')
def homepage():
    return render_template('homepage.html')