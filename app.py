import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    pad = Path(__file__).with_name("links.json")
    data = json.loads(pad.read_text(encoding="utf-8"))
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
