# View functions
from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm
from flask_login import current_user
from app.models import User
from app import app, db


@app.route('/')
def index():
    feed_blank = 'Podcast Main page: RSS feed'
    return render_template('index.html', feed_blank=feed_blank)


@app.route('/')
def login():
    pass


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
        flash(f'Ваш аккаунт успешно создан. Теперь Вы можете войти:', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)
