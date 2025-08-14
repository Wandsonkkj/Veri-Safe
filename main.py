from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('app/config.py')
csrf = CSRFProtect(app=app)

from app.views import * 

if __name__ == '__main__':
    app.run(debug=True)