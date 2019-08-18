from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,\
    ValidationError

from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        'Имя пользователя',
        render_kw={"placeholder": "Ваше имя пользователя"},
        validators=[
            DataRequired(),
            Length(min=2, max=64)])
    email = StringField(
        'Почтовый ящик',
        render_kw={"placeholder": "you@example.com"},
        validators=[
            DataRequired(),
            Email()])
    password = PasswordField(
        'Пароль',
        validators=[
            DataRequired(),
            Length(min=3, max=25)])
    confirm_password = PasswordField(
        'Подтверждение пароля',
        validators=[
            DataRequired(),
            Length(min=3, max=25),
            EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    @staticmethod
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Это имя пользователя уже занято. Пожалуйста \
            выберите другое.')

    @staticmethod
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Этот почтовый ящик уже занят. Пожалуйста \
            выберите другое.')

            
class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class UploadJokeForm(FlaskForm):
    text = StringField('Текст', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class EditJokeForm(FlaskForm):
    text = StringField("Текст", validators=[DataRequired()])
    submit = SubmitField("Редактировать")
