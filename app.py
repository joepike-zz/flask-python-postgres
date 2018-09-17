
from flask import Flask, render_template, request
from models import db, User
import os

app = Flask(__name__)

# POSTGRES = {
#     'user': 'joe',
#     'pw': 'password',
#     'db': 'my_database',
#     'host': 'localhost',
#     'port': '5432',
# }

POSTGRES = {
    'user': os.environ.get('POSTGRES_USER'),
    'pw': os.environ.get('POSTGRES_PASSWORD'),
    'db': os.environ.get('POSTGRES_DB'),
    'host': os.environ.get('POSTGRES_HOST') or 'localhost',
    'port': os.environ.get('POSTGRES_PORT') or '5432',
}

app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(POSTGRES['user'], POSTGRES['pw'], POSTGRES['host'], POSTGRES['port'], POSTGRES['db'])
print app.config['SQLALCHEMY_DATABASE_URI']

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    username = request.form['username']
    email = request.form['email']
    print email
    print username

    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')

    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    users = User.query.all()
    print users

    return render_template('greeting.html', username=request.form['username'], email=request.form['email'])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
