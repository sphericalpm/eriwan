from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class FileUploadForm(FlaskForm):
    file = FileField('Upload podcast', validators=[
        FileRequired(),
        FileAllowed(['mp3'], "Wrong format! Only mp3 format audio files")
    ])
