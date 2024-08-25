from flask import Flask, render_template, request

app = Flask(__name__)

storage = []

@app.route('/', methods=['GET', 'POST'])
def home():
    mens = 'aaa'
    if request.method == 'POST':  
        usuario = request.form.get('login') 
        senha = request.form.get('pass')
        if usuario and senha: 
            client = {'login': usuario, 'pass': senha}
            storage.append(client)
            mens = 'Você foi cadastrado'
            return redirecionar
    return render_template('main/cadastro.html', mensagem=mens)

@app.route('/', methods = ['POST'])
def redirecionar():
    return render_template('administrador/teste.html')

if __name__ == '__main__':
    app.run(debug=True)
