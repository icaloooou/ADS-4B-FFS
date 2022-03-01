import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# configuracoes MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '475869'
app.config['MYSQL_DATABASE_DB'] = 'testes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

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
            cursor.execute('INSERT INTO project_mvc(name, password, email) VALUES (%s, %s, %s);', (_name, _password, _email))
            conn.commit()

    except Exception as error:
        print('Problema de inserção no banco de dados: '+ str(error))
    finally:
        return render_template('layoutlogin.html')

@app.route('/list', methods=['POST', 'GET'])
def listagem():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('SELECT name, email, password FROM project_mvc')
    data = cursor.fetchall()

    return render_template('list.html', data=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)