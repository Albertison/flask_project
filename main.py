from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def mainium():
    params = {}
    params['title'] = 'Начало'
    return render_template('first_page.html', **params)


@app.route("/about_us")
def about_us():
    return render_template("about_us.html", title='Про нас')


@app.route('/game')
def game():
    return render_template("game.html", title="Начало игры")


@app.route('/obnovlenia')
def obnovlenia():
    return render_template('obnovlenia.html', title='Обновления')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
