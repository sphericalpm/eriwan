# Config Classes

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Wo7GhuD2OWIv'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMINS = ['your-email@example.com']

    STATIC_ROOT = '/static/'

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024
    UPLOAD_PODCAST_FOLDER = 'episodes'