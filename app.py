from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'segredo123'  # Troque por uma chave segura

usuarios = {"admin": "1234"}  # Usuário e senha fixos

@app.route('/', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        senha = request.form['senha']
        if senha == usuarios["admin"]:
            session['logado'] = True
            return redirect('/dashboard')
        else:
            erro = "Senha incorreta!"
    return render_template('login.html', erro=erro)

@app.route('/dashboard')
def dashboard():
    if not session.get('logado'):
        return redirect('/')
    # Simulação de dados (depois podemos puxar do banco)
    responsaveis = ["João", "Maria", "Carlos"]
    tipos = ["Mensal", "Trimestral"]
    balancetes = [
        {"responsavel": "João", "tipo": "Mensal", "mes": "Março", "msc_reo": False, "rgf": False, "protocolo_tce": "", "pendencias": ""}
    ]
    return render_template('dashboard.html', responsaveis=responsaveis, tipos=tipos, balancetes=balancetes)

if __name__ == '__main__':
    app.run(debug=True)
