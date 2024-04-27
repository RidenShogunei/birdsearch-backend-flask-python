
from . import db
class User(db.Model):
    uid = db.Column(db.String(200), primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    realname = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

