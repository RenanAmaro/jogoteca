import os
SECRET_KEY = 'alura'

SGBD = 'mysql+mysqlconnector'
usuario = 'root'
senha = 'bogio1986'
servidor = 'localhost'
database = 'db_jogoteca'

SQLALCHEMY_DATABASE_URI = \
    f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__))+'/uploads'