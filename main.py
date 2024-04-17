from flask import Flask
from flask import render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Entrance')


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if check_password(username, password):
            return redirect('/success')
        else:
            return render_template('login.html', title='Авторизация', form=form, message="Неверные учетные данные")
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/")
def mainium():
    return render_template('first_page.html', title='Начало')


@app.route('/en')
def mainium_en():
    return render_template('first_page_en.html', title='Beginning')


@app.route("/about_us")
def about_us():
    return render_template("about_us.html", title='Про нас')


@app.route("/about_us_en")
def about_us_en():
    return render_template("about_us_en.html", title='About us')


@app.route('/game')
def game():
    return render_template("game.html", title="Начало игры")


@app.route('/game_en')
def game_en():
    return render_template("game_en.html", title="Начало игры")


@app.route('/obnovlenia')
def obnovlenia():
    return render_template('obnovlenia.html', title='Обновления')


@app.route('/obnovlenia_en')
def obnovlenia_en():
    return render_template('obnovlenia_en.html', title='Updates')


@app.route('/game/rules')
def mrorii_1():
    return render_template('mrorii_1.html', title="Мрорий")


@app.route('/game_en/rules')
def mrorii_1_en():
    return render_template('mrorii_1_en.html', title="Mrorii")


@app.route('/game/rules/1')
def hist_1():
    return render_template('hist_1_1.html')


@app.route('/game_en/rules/1')
def hist_1_en():
    return render_template('hist_1_1_en.html')


@app.route('/game/rules/dontunderstand')
def dontunderstand():
    return render_template('dontunderstand.html')


@app.route('/game/rules/understand')
def understand():
    return render_template('understand.html')


@app.route('/game/rules/understand_en')
def understand_en():
    return render_template('understand_en.html')


@app.route('/game/rules/dontunderstand_en')
def dontunderstand_en():
    return render_template('dontunderstand_en.html')


@app.route('/game/first_story/room')
def first_story_room():
    return render_template('first_story_room.html')


@app.route('/game/first_story/room/switchon')
def first_story_room_switchon():
    return render_template('first_story_room_switchon.html')


@app.route('/game/first_story/room/switchoff')
def first_story_room_switchoff():
    return render_template('first_story_room_switchoff.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
