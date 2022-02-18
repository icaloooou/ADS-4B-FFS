import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('calcula.html')

@app.route('/calculaform', methods=['POST'])
def calculadora():
    valor1 = request.form['valor1']
    valor2 = request.form['valor2']
    operacao = request.form['operacao']

    v1 = int(valor1)
    v2 = int(valor2)

    if operacao == '+':
        resultado = v1 + v2
    elif operacao == '-':
        resultado = v1 - v2
    elif operacao == '*':
        resultado = v1 * v2
    elif operacao == '/':
        if v2 == 0:
            resultado = 'Operação de divisão com zero'
        else:
            resultado = v1 / v2         
    else:
        resultado = 'Operação não reconhecida, tente com +, -, * ou /'
    return str(resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)