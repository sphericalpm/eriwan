import os
from pathlib import Path

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import app, db, login_manager
from .utils import concatenate_audios


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Episode id: {self.id}>, name: {self.name}'

    def get_file_path(self):
        '''
        Return wrapped in jingles file path
        '''
        static_path = os.path.join(app.config.get('STATIC_ROOT'), 'episodes')
        file_path = f'{static_path}/{self.id}.mp3'
        if os.path.exists(file_path):
            return file_path

    # todo: add to celery task
    def generate_wrapped_file(self, episode_path, name_path):
        """
        Concatenate episode name audio and episode audio
        :param episode_path: path to episode mp3
        :param name_path: path to episode name mp3
        :return:
        """
        static_path = os.path.join(app.config.get('STATIC_ROOT'), 'episodes')

        if not os.path.exists(static_path):
            os.mkdir(static_path)

        file_path = f'{static_path}/{self.id}.mp3'
        concatenate_audios([name_path, episode_path], file_path)

    def get_link(self):
        static = app.config.get('STATIC_ROOT') + f'{self.id}.mp3'
        file_path = Path(static)
        host = app.config.get('HOST', 'localhost:5000')
        return 'http://' + host + file_path.as_posix()


class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke_text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Episode id: {self.id}>, name: {self.joke_text}'

    def get_file_path(self):
        '''
        Return wrapped in jingles file path
        '''
        static_path = os.path.join(app.config.get('STATIC_ROOT'), 'jokes')
        file_path = f'{static_path}/{self.id}.mp3'
        if os.path.exists(file_path):
            return file_path

    def generate_base_file(self):
        '''
        Return generate base audio file from joke_text
        '''
        pass

    # todo: add to celery task
    def generate_wrapped_file(self, joke_path):
        """
        generate wrapped in jingles file from joke_path
        :param joke_path: path to joke mp3
        :return:
        """
        static_path = os.path.join(app.config.get('STATIC_ROOT'), 'jokes')
        if not os.path.exists(static_path):
            os.mkdir(static_path)

        file_path = f'{static_path}/{self.id}.mp3'
        jingle_path = os.path.join(app.config.get('STATIC_ROOT'), "jingles", "jingle.mp3")

        concatenate_audios([jingle_path, joke_path, jingle_path], file_path)
