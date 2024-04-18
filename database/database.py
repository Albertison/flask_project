from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient(
    'mongodb+srv://pirsovvasa:m7HxfAsmffsG6bZ6@donut.7o74pyh.mongodb.net/?retryWrites=true&w=majority&appName=donut')

db = client['donutDB']

users = db['donut']


def add_user(username, password, email):
    user_data = {
        'username': username,
        'password': generate_password_hash(password),
        'email': email
    }
    return users.insert_one(user_data)


def user_exists(username):
    return users.find_one({'username': username}) is not None


def check_password(username, password):
    user = users.find_one({'username': username})
    return user and check_password_hash(user['password'], password)