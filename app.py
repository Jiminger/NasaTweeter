from flask import Flask, render_template
import db_controller

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", img_url=(db_controller.get_row('apod')[3]))
