# View functions
from flask import render_template, flash, session
from app import app
from app.forms import UploadJokeForm
from app.models import Joke
from app import db


@app.route('/')
def index():
    feed_blank = 'Podcast Main page: RSS feed'
    return render_template('index.html', feed_blank=feed_blank)


@app.route('/add_joke', methods=['GET', 'POST'])
def add_joke_template():
    form = UploadJokeForm()
    if form.validate_on_submit():
        new_joke = Joke(joke_text=form.text.data)
        db.session.add(new_joke)
        db.session.commit()
        flash('Шутка добавлена!')
    return render_template('add_joke.html', form=form)
