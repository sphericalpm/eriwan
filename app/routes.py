# View functions
from flask import render_template, url_for, redirect
from werkzeug.datastructures import CombinedMultiDict
from flask import request
from werkzeug.utils import secure_filename
from flask_login import current_user, login_required

from app import app
from .forms import FileUploadForm
from .models import Episode
from app import db


@app.route('/')
def index():
    feed_blank = 'Podcast Main page: RSS feed'
    form = FileUploadForm()
    return render_template('index.html', feed_blank=feed_blank, form=form)


@login_required
@app.route('/upload-podcast', methods=['POST'])
def upload_file():
    form = FileUploadForm(CombinedMultiDict((request.files, request.form)))
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
