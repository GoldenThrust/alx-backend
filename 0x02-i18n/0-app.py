#!/usr/bin/env python3
""" internationalization Flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """The home page."""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
