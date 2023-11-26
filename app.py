from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    context = {'active': 'index'}
    return render_template('index.html', **context)

@app.route('/pc/')
def pc():
    conn = sqlite3.connect('sqlite.db')
    cur = conn.cursor()
    query = "select name, photo, game, photi, gami FROM games"
    cur.execute(query)

    games = []
    for name, photo, game, photi, gami in cur.fetchall():
        games.append({
            "name": name,
            "photo": photo,
            "game": game,
            "photi": photi,
            "gami": gami,
        })
    cur.close()
    conn.close()
    context = {
        'active': 'pc',
        "games": games
    }
    return render_template('pc.html', **context)

@app.route('/mobile/')
def mobile():
    conn = sqlite3.connect('sqlite.db')
    cur = conn.cursor()
    query = "select name, photo, game, photi, gami FROM mobile"
    cur.execute(query)

    mobile = []
    for name, photo, game, photi, gami in cur.fetchall():
        mobile.append({
            "name": name,
            "photo": photo,
            "game": game,
            "photi": photi,
            "gami": gami,
        })
    cur.close()
    conn.close()
    context = {
        'active': 'mobile',
        "mobile": mobile
    }
    return render_template('mobile.html', **context)

@app.route('/obo/')
def obo():
    context = {'active': 'obo'}
    return render_template('obo.html', **context)

if __name__ == "__main__":
     app.run()