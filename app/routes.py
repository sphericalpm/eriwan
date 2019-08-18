from flask import render_template, url_for, flash, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename

from app.forms import RegistrationForm, UploadJokeForm, LoginForm, EpisodeUploadForm
from app.models import User, Joke, Episode
from app import app, db

from werkzeug.urls import url_parse


@app.route('/')
def index():
    feed_blank = 'Podcast Main page: RSS feed'
    form = EpisodeUploadForm()
    return render_template('index.html', feed_blank=feed_blank, form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(('Ваш аккаунт успешно создан. Теперь Вы можете войти:'), category='info')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)

  
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


@app.route('/add_joke', methods=['GET', 'POST'])
def add_joke_template():
    form = UploadJokeForm()
    if form.validate_on_submit():
        new_joke = Joke(joke_text=form.text.data)
        db.session.add(new_joke)
        db.session.commit()
        flash('Шутка добавлена!')
    return render_template('add_joke.html', form=form)


@login_required
@app.route('/upload-podcast', methods=['POST'])
def upload_file():
    form = EpisodeUploadForm(CombinedMultiDict((request.files, request.form)))
    if form.validate():
        filename = secure_filename(form.file.data.filename)
        episode = Episode(
            name=filename.rstrip('.mp3'),
            user_id=current_user.get_id()
        )
        upload_folder = app.config['UPLOAD_PODCAST_FOLDER']
        static_path = app.config['STATIC_ROOT']
        form.file.data.save(f'{static_path}{upload_folder}/{episode.id}')
        db.session.add(episode)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
