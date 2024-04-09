#!/usr/bin/env python3
"""
A basic Flask app
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config(object):
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    returns a user dictionary or None if the ID cannot be found
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request() -> None:
    """
    If user is found it adds them to flask.g
    """
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route to index
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """
    A locale selector for the Babel extension in Flask
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
