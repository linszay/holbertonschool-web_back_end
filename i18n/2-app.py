#!/usr/bin/env python3
"""creating a simple flask app task 1"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locales():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """rendering the index.html template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
