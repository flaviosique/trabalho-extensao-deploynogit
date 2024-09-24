from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    return redirect(url_for('obrigado'))

@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')

if __name__ == '__main__':
    app.run(debug=True)
