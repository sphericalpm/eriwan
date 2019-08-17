# View functions
from flask import render_template
from app import app
from .forms import FileUploadForm


@app.route('/')
def index():
    feed_blank = 'Podcast Main page: RSS feed'
    return render_template('index.html', feed_blank=feed_blank)


@app.route('/upload-podcast/', methods=['POST'])
def upload_file():
    form = FileUploadForm(request.form)
    if form.validate():
        pass
    return render_template('index.html', form=form)
