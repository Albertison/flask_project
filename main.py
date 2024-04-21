from flask import Flask, request
from flask import render_template
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
        return render_template('oshibka1.html')


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'GET':
        return render_template('enter.html', title='Начало')
    elif request.method == 'POST':
        if database.user_exists(request.form['text']):
            if database.check_password(request.form['text'], request.form['password']):
                return render_template('str2.html')
            return render_template('oshibka2.html')
        return render_template('oshibka3.html')


@app.route("/")
def mainium():
    return render_template('first_page.html', title='Начало')


@app.route("/er")
def mainium2():
    return render_template('first_page2.html', title='Начало')


@app.route("/rew")
def mainium3():
    return render_template('first_page3.html', title='Наало')


@app.route("/about_us")
def about_us():
    return render_template("about_us.html", title='Про нас')


@app.route("/about_us2")
def about_us2():
    return render_template("about_us2.html", title='Про нас')


@app.route("/about_us3")
def about_us3():
    return render_template("about_us3.html", title='Про нас')


@app.route('/game')
def game():
    return render_template("game.html", title="Начало игры")


@app.route('/obnovlenia')
def obnovlenia():
    return render_template('obnovlenia.html', title='Обновления')


@app.route('/obnovlenia2')
def obnovlenia2():
    return render_template('obnovlenia2.html', title='Обновления')


@app.route('/obnovlenia3')
def obnovlenia3():
    return render_template('obnovlenia3.html', title='Обновления')


@app.route('/game/rules')
def mrorii_1():
    return render_template('mrorii_1.html', title="Мрорий")


@app.route('/game/rules/1')
def hist_1():
    return render_template('hist_1_1.html')


@app.route('/game/rules/dontunderstand')
def dontunderstand():
    return render_template('dontunderstand.html')


@app.route('/game/rules/understand')
def understand():
    return render_template('understand.html')


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


@app.route('/game/nojnoi_dozor_prolog_2_gohome')
def nojnoi_dozor_prolog_2_gohome():
    return render_template('nojnoi_dozor_prolog_2_gohome.html')
