from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://blog:chen2003@47.96.160.149/birdsearch'
db = SQLAlchemy(app)

class User(db.Model):
    uid = db.Column(db.String(200), primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    realname = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

def test_db_connection():
    with app.app_context():
        try:
            db.session.query(User).first()
            print("Database connected!")
        except OperationalError as e:
            print("Could not connect to Database.")
            print(f"Error details: {e}")

@app.route('/')
def hello_world():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)  # ssl_context=('cert.pem', 'key.pem') 已被注释掉