#!/usr/bin/env python3
"""
A basic Flask app
"""
from flask_babel import Babel
from flask import Flask, render_template, request


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


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route to index
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    A locale selector for the Babel extension in Flask
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
