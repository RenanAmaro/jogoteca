from flask import Flask, redirect, render_template, request, session, flash

# criar uma classe Jogo com os atributos nome, categoria, console


class Jogo():
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)
app.secret_key = 'alura'

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
        return redirect('/login?proxima=novo')

    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')

    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'teste' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f'{session["usuario_logado"]} logado com sucesso!')
        proxima_pagina = request.form['proxima']
        if proxima_pagina == 'None':
            return redirect(f'/')
        else:
            return redirect(f'/{proxima_pagina}')
    else:
        flash('Usuário não logado')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')


app.run(debug=True)
# app.run(host='0.0.0.0', port=8080)
