import os
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db
from .audio_utils import concatenate_audios, text_to_speech


class User(db.Model):
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
    def generate_wrapped_file(self, episode_path):
        """
        Concatenate an episode name mp3 file and an episode mp3 file
        :param episode_path: path to episode mp3
        """

        name_path = text_to_speech(self.name, self.name)
        concatenate_audios([name_path, episode_path], name_path)


class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke_text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Episode id: {self.id}>, name: {self.name}'

    def get_file_path(self):
        '''
        Return wrapped in jingles file path
        '''
        static_path = os.path.join(app.config.get('STATIC_ROOT'), 'jokes')
        file_path = f'{static_path}/{self.id}.mp3'
        if os.path.exists(file_path):
            return file_path

    def generate_base_file(self):
        """
        Generate wrapped in jingles mp3 file from joke_text
        """
        temp_path = text_to_speech(self.joke_text)
        jingle_path = os.path.join(
            app.config.get('STATIC_ROOT'), "jingles", "jingle.mp3"
        )

        concatenate_audios([jingle_path, temp_path, jingle_path], 'jokes')
