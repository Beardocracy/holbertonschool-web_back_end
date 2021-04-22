#!/usr/bin/env python3
''' Basic flask app '''
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    ''' Babel Configs '''
    LANGUAGES = ['en', 'fr']


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)

babel = Babel(app)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@app.route('/', methods=['GET'])
def welcome():
    '''
    GET
    Return: Render template
    '''
    return render_template('6-index.html', user=g.user)


@babel.localeselector
def get_locale():
    ''' Requests best match for supported languages '''

    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale

    user = request.args.get('login_as')
    if user:
        locale = get_user(user).get('locale')
        if locale in Config.LANGUAGES:
            return locale

    header = request.headers.get('locale')
    if header:
        return header

    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user(user_num):
    ''' Finds user '''
    if user_num and int(user_num) in users:
        return users.get(int(user_num))


@app.before_request
def before_request():
    ''' Get user '''
    g.user = get_user(request.args.get('login_as'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
