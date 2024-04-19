from flask import Flask, request
from flask import render_template, redirect
from database import database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Начало')
    elif request.method == 'POST':
        if not database.user_exists(request.form['text']):
            database.add_user(request.form['text'], request.form['password'], request.form['email'])
            return render_template('str.html')


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'GET':
        return render_template('enter.html', title='Начало')
    elif request.method == 'POST':
        if database.user_exists(request.form['text']):
            if database.check_password(request.form['text'], request.form['password']):
                return render_template('str.html')


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


@app.route('/game/first_story/room/first_story_room_truth')
def first_story_room_truth():
    return render_template('first_story_room_truth.html')


@app.route('/game/first_story/room/first_story_room_lier')
def first_story_room_lier():
    return render_template('first_story_room_lier.html')


@app.route('/game/nojnoi_dozor_prolog_1')
def nojnoi_dozor_prolog():
    return render_template('nojnoi_dozor_prolog_1.html')
