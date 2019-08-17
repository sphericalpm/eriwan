from flask import render_template, url_for, redirect, flash, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import app, db
from app.forms import UploadJokeForm, LoginForm
from app.models import Joke, User


@app.route('/')
def index():
    feed_blank = 'Podcast Main page: RSS feed'
    return render_template('index.html', feed_blank=feed_blank)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid Username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = '/index'
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register')
def register():
    pass


@app.route('/add_joke', methods=['GET', 'POST'])
def add_joke_template():
    form = UploadJokeForm()
    if form.validate_on_submit():
        new_joke = Joke(joke_text=form.text.data)
        db.session.add(new_joke)
        db.session.commit()
        flash('Шутка добавлена!')
    return render_template('add_joke.html', form=form)
