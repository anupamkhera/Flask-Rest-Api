import sqlite3
from db import db
# model is internal representation of entity , , like a helper
# resource is external representation of entity, api responds with resources
class UserModel(db.Model):# not a resource used to help in storin ,retreving data from db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first() #select * from users

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first() #select * from users
