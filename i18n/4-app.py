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
def get_locale():
    """force a locale with URL param"""
    req_locale = request.args.get('locale')
    if req_locale in app.config['LANGUAGES']:
        return req_locale
    """request.accept_languages determines best match with our languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """rendering the index.html template"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
