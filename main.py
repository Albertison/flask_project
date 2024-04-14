from flask import Flask
from flask import render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
