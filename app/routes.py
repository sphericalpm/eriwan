# View functions
from flask import render_template, url_for, redirect
from werkzeug.datastructures import CombinedMultiDict
from flask import request
from werkzeug.utils import secure_filename

from app import app
from .forms import FileUploadForm


@app.route('/')
def index():
    feed_blank = 'Podcast Main page: RSS feed'
    form = FileUploadForm()
    return render_template('index.html', feed_blank=feed_blank, form=form)


@app.route('/upload-podcast', methods=['POST'])
def upload_file():
    form = FileUploadForm(CombinedMultiDict((request.files, request.form)))
    if form.validate():
        filename = secure_filename(form.file.data.filename) # app.config['UPLOAD_PODCAST_FOLDER']
        upload_folder = app.config['UPLOAD_PODCAST_FOLDER']
        form.file.data.save(f'{upload_folder}/{filename}')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
