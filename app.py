
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

@app.route('/', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('greeting.html', username=request.form['username'], email=request.form['email'])

if __name__ == '__main__':
    app.run()
