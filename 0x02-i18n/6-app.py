#!/usr/bin/env python3
""" internationalization Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config:
    """app configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Retrieves the best match with
    our supported languages."""
    r_locale = request.args.get("locale")
    if r_locale and r_locale in app.config["LANGUAGES"]:
        return r_locale
    u_locale = g.user.get("locale")
    if u_locale and u_locale in app.config["LANGUAGES"]:
        return u_locale
    h_locale = request.headers.get("locale")
    if h_locale and h_locale in app.config["LANGUAGES"]:
        return h_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """Return user information from current user"""
    id = request.args.get("login_as")

    if id:
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """before_request function"""
    g.user = get_user()


@app.route("/")
def index():
    """The home page."""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
