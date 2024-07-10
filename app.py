from typing import Required
from flask import Flask, render_template
from pony.orm import Database, db_session


app = Flask(__name__)

""
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mapa")
def mapa():
    return render_template("mapa.html")

if __name__ == "__main__":
    app.run(debug=True)