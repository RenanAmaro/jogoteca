from flask import Flask, redirect, render_template, request, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

# criar uma classe Jogo com os atributos nome, categoria, console


class Jogo():
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario():
    def __init__(self, nome, nickname, senha) -> None:
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


renan = Usuario('Renan', 'Lindo', 'teste')
fabiana = Usuario('Fabiana', 'Mozao', 'teste2')
enzo = Usuario('Enzo', 'Furacao', 'teste3')

usuarios = {
    renan.nickname: renan,
    fabiana.nickname: fabiana,
    enzo.nickname: enzo
}

app = Flask(__name__)
app.secret_key = 'alura'

SGBD = 'mysql+mysqlconnector'
usuario = 'root'
senha = 'bogio1986'
servidor = 'localhost'
database = 'tb_jogoteca'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'{SGBD}://{usuario}:{senha}@{servidor}/{database}'

db = SQLAlchemy(app)


class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(8), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


lista = []
j1 = Jogo('God of War', 'RPG', 'PS4')
lista.append(j1)
j2 = Jogo('Fifa', 'Esporte', 'Xbox')
lista.append(j2)
j3 = Jogo('Mortal Combate', 'Luta', 'PS2')
lista.append(j3)


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))

    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')

    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario in usuarios:
        if senha == usuarios[usuario].senha:
            session['usuario_logado'] = usuarios[usuario].nickname
            flash(f'{usuarios[usuario].nickname} logado com sucesso!')
        proxima_pagina = request.form['proxima']
        # if proxima_pagina == 'None':
        #     return redirect(url_for('index'))
        # else:
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)
# app.run(host='0.0.0.0', port=8080)
