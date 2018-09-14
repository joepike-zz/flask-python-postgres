
from flask import Flask, render_template, request
from models import db

app = Flask(__name__)

POSTGRES = {
    'user': 'joe',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST'])
def signUP():

    _username = request.form['inputName']
    _email = request.form['inputEmail']

@app.route('/')
def main():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
