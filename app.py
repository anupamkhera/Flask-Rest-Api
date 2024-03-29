import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL?sslmode=require', 'sqlite:///data.db').replace('postgres://', 'postgresql://') #environment variable and default variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key ='jose'
api = Api(app)


jwt = JWT(app, authenticate, identity) #/auth

items = []

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ =='__main__': # only execute app.run if called from app.py not from other file by importing
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
