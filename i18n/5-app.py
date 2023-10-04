#!/usr/bin/env python3
"""creating a simple flask app task 1"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.before_request
def before_request():
    """executed before other funcs & sets user as a global var"""
    g.user = get_user()


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """finds user and gets user_id"""
    user_id = int(request.args.get('login_as', 0))
    return users.get(user_id)


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
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
