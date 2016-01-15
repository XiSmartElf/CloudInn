from flask import render_template, flash, redirect, url_for
from Site import app
from .forms import LoginForm

from oauth import OAuthSignIn
from models import User
from models import db
from flask_login import login_user, logout_user, current_user, LoginManager


lm = LoginManager(app)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/authenticate')
def authenticate():
    user = {'nickname': 'Lan'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'Master He'},
            'body': 'DAS NAS SAN, what the frack?!'
        },
        {
            'author': {'nickname': 'Jefferey'},
            'body': 'Facebook react is a whooh!'
        }
    ]
    return render_template("index.html",
                           title='CloudInn',
                           user=user,
                           posts=posts)

@app.route('/index')
def welcome():
    return "welcome to index!"



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template("login.html",
                           title='Sign In',
                           form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))