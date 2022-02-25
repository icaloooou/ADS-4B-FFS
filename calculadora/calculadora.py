import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('calcula.html')

@app.route('/calculaform', methods=['POST'])
def calculadora():
    valor1 = int(request.form['valor1'])
    valor2 = int(request.form['valor2'])
    operacao = request.form['operacao']

    if operacao == '+':
        resultado = valor1 + valor2
    elif operacao == '-':
        resultado = valor1 - valor2
    elif operacao == '*':
        resultado = valor1 * valor2
    elif operacao == '/':
        if valor2 == 0:
            resultado = 'Operação de divisão com zero, tente novamente com outro número'
        else:
            resultado = valor1 / valor2         
    else:
        resultado = 'Operação não reconhecida, tente com +, -, * ou /'
    return str(resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)