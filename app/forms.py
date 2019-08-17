from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UploadJokeForm(FlaskForm):
    text = StringField('Текст', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
