# View functions
from flask import render_template, redirect, url_for
from werkzeug.datastructures import CombinedMultiDict
from flask import request

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
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

