from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/admin', methods=['GET', 'POST'])
def home():
    nome = None
    if request.method == 'POST':  
        nome = request.form.get('nome') 
        if(nome != "None" and nome == "aaa"):
            mensagem = "Olá, {nome}"
            return render_template('main/cadastro.html')

        else:
            mensagem = "Digite um nome para se cadastrar"
    return render_template('teste.html', name=nome)
   

if __name__ == '__main__':
    app.run(debug=True, port=5050)
