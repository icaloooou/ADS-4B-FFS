import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# configuracoes MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '475869'
app.config['MYSQL_DATABASE_DB'] = 'testes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showlogin')
def showlogin():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        _name = request.form['name']
        _email = request.form['email']
        _password = request.form['password']
    
        #verificar credenciais
        if _name and _email and _password:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO project_mvc VALUES (%s, %s, %s);', (_name, _email, _password))
            conn.commit()

    except Exception as error:
        print('Problema de inserção no banco de dados: '+ str(error))
    finally:
        return render_template('index.html')

@app.route('/lista', methods=['GET'])
def listagem():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('SELECT name, email FROM project_mvc')
    data = cursor.fetchall()

    return render_template('lista.html', data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)