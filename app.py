from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import requests
import os


app = Flask(__name__)

DB = "productivity.db"

# ------------------ DATABASE ------------------
def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ------------------ ROUTES ------------------
@app.route("/")
def index():
    conn = get_db()
    todos = conn.execute("SELECT * FROM todos").fetchall()
    conn.close()

    weather = get_weather("Dubai")  # change city if you want
    return render_template("index.html", todos=todos, weather=weather)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        conn = get_db()
        conn.execute("INSERT INTO todos (task) VALUES (?)", (task,))
        conn.commit()
        conn.close()
    return redirect(url_for("index"))

@app.route("/toggle/<int:id>")
def toggle(id):
    conn = get_db()
    conn.execute("""
        UPDATE todos
        SET done = CASE WHEN done = 1 THEN 0 ELSE 1 END
        WHERE id = ?
    """, (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM todos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


def get_weather(city):
    api_key = os.environ.get("OPENWEATHER_API_KEY")  # replace with your OpenWeatherMap API key
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )
    try:
        r = requests.get(url, timeout=5)
        data = r.json()
        return {
            "city": city,
            "temp": data["main"]["temp"],
            "desc": data["weather"][0]["description"].title()
        }
    except Exception:
        return None

if __name__ == "__main__":
    app.run(debug=True)
