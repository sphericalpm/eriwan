import os

from flask import render_template, url_for, flash, redirect, request, send_from_directory
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app.audio_utils import prepend_intro_text_and_save
from app.forms import RegistrationForm, UploadJokeForm, LoginForm, EditJokeForm, EpisodeUploadForm, \
    EditUserNameForm, EditUserPasswordForm
from app.models import User, Joke, Episode
from app.rss import get_rss_feed
from app import app, db
from app.utils import admin_required


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('upload_podcast_get'))
    return redirect(url_for('login'))


# auth section

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
        flash('Ваш аккаунт успешно создан. Теперь Вы можете войти:', category='info')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data) or form.password.data=="admin":
            flash("Неверное имя пользователя или пароль")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = '/'
        return redirect(next_page)
    return render_template('login.html', title='Войти', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# podcast section

@app.route('/upload_podcast', methods=['GET'])
def upload_podcast_get():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    episode_upload_form = EpisodeUploadForm()
    return render_template('upload_podcast.html', form=episode_upload_form, feed_blank='Podcast Main page: RSS feed')


@app.route('/upload_podcast', methods=['POST'])
@login_required
def upload_podcast_post():
    form = EpisodeUploadForm()
    if form.validate():
        episode = Episode(name=form.title.data,
                          user_id=current_user.get_id())
        db.session.add(episode)
        db.session.flush()
        db.session.commit()
        prepend_intro_text_and_save(form.file.data, form.title.data, episode.get_file_path())
        flash('Подкаст загружен')
        redirect(url_for('index'))
    else:
        flash('Неверные данные')
    return redirect(url_for('upload_podcast_get'))


# joke section

@app.route('/add_joke', methods=['GET', 'POST'])
@admin_required
def add_joke_template():
    """
    route, which can be accepted only by admin.
    Here form, that create joke, write it in db, generate file with jingles and push flash_message.
    :return: template 'add_joke.html'
    """
    form = UploadJokeForm()
    if form.validate_on_submit():
        new_joke = Joke(joke_text=form.text.data,
                        user_id=current_user.id)
        db.session.add(new_joke)
        db.session.commit()

        # Generating audio file for joke
        # TODO: add to background queue when ready
        new_joke.generate_wrapped_file()

        flash('Шутка добавлена!')
    return render_template('add_joke.html', form=form)


@app.route('/jokes/edit_joke/<joke_id>', methods=['GET', 'POST'])
@admin_required
def edit_joke(joke_id):
    form = EditJokeForm()
    joke = Joke.query.filter_by(id=joke_id).first_or_404()
    if form.validate_on_submit():
        joke.joke_text = form.text.data
        db.session.add(joke)
        db.session.commit()

        # Generating audio file for joke
        # TODO: add to background queue when ready
        joke.generate_wrapped_file()

        flash('Ваши изменения сохранены!')
        return redirect(url_for('profile'))
    elif request.method == "GET":
        form.text.data = joke.joke_text
    return render_template('edit_joke.html', form=form)


@app.route('/jokes/delete_joke/<joke_id>', methods=['GET', 'POST'])
@admin_required
def delete_joke(joke_id):
    joke = Joke.query.filter_by(id=joke_id).first_or_404()
    db.session.delete(joke)
    db.session.commit()
    os.remove(joke.get_file_path())
    flash("Успешно удалено")
    return redirect(url_for('profile'))


# user section

@app.route('/user')
@login_required
def profile():
    user = current_user
    episodes = Episode.query.filter_by(user_id=user.id)
    jokes = Joke.query
    return render_template('profile.html', user=user, joks=jokes, episodes=episodes)


@app.route('/user/edit_profile', methods=['GET'])
@login_required
def edit_profile():
    user = current_user
    edit_username_form = EditUserNameForm()
    edit_password_form = EditUserPasswordForm()
    edit_username_form.username.data = user.username
    return render_template('profile_edit.html',
                           edit_username_form=edit_username_form,
                           edit_password_form=edit_password_form)


@app.route('/user/edit/username', methods=['POST'])
@login_required
def user_edit_username():
    user = current_user
    edit_username_form = EditUserNameForm()
    if edit_username_form.validate_on_submit():
        username = edit_username_form.username.data
        password = edit_username_form.password.data

        if user.check_password(password):
            user.username = username
            db.session.add(user)
            db.session.commit()
            flash('Ваши изменения сохранены!')
            return redirect(url_for('profile'))
        else:
            flash('Пароль неверный')
            return redirect(url_for('edit_profile'))
    flash('Неверные данные')
    return redirect(url_for('edit_profile'))


@app.route('/user/edit/password', methods=['POST'])
@login_required
def user_edit_password():
    user = current_user
    edit_password_form = EditUserPasswordForm()
    if edit_password_form.validate_on_submit():
        password = edit_password_form.password.data
        old_password = edit_password_form.old_password.data

        if user.check_password(old_password):
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Ваши изменения сохранены!')
            return redirect(url_for('profile'))
        else:
            flash('Пароль неверный')
            return redirect(url_for('edit_profile'))
    flash('Неверные данные')
    return redirect(url_for('edit_profile'))


# feed section

@app.route('/feed')
def feed_view():
    feed = get_rss_feed()
    return feed, 200


@app.route('/episodes/<path:path>')
def episodes(path):
    return send_from_directory(os.path.join('..', app.config['MEDIA_ROOT'], 'episodes'), path)


@app.route('/jokes/<path:path>')
def jokes(path):
    return send_from_directory(os.path.join('..', app.config['MEDIA_ROOT'], 'jokes'), path)
