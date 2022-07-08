from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# criar uma classe Jogo com os atributos nome, categoria, console

app = Flask(__name__)
from views import *
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
