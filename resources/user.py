import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
class UserRegister(Resource): # it is a resource or create endpoint

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field can not be blank."
        )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This field can not be blank."
        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message" : "A user with the username already exists"}, 400

        user = UserModel(**data) #(data['username'], data['password'])
        user.save_to_db()

        return {"message" : "User created successfully."}, 201
