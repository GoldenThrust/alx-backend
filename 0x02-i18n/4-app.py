from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config:
    """ app configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """ Retrieves the best match with
    our supported languages. """
    user = getattr(g, 'user', None)
    print(g)
    if user is None:
        # if user.local in app.config["LANGUAGES"]:
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """The home page."""
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)