import json
from pathlib import Path

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    pad = Path(__file__).with_name("links.json")
    data = json.loads(pad.read_text(encoding="utf-8"))
    return render_template("index.html", data=data)

@app.route("/sw.js")
def service_worker():
    resp = send_from_directory("static","sw.js")
    resp.headers["Cache-Control"] = "no-cache"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
