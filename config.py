# Config Classes

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Wo7GhuD2OWIv'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMINS = ['your-email@example.com']

    STATIC_ROOT = 'static/'
    MEDIA_ROOT = 'media/'
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024
    UPLOAD_PODCAST_FOLDER = 'episodes'

    DROPZONE_DEFAULT_MESSAGE = 'Перетащите аудио файл в эту зону для загрузки'
    DROPZONE_MAX_FILE_SIZE = 20
    DROPZONE_INVALID_FILE_TYPE = 'Только аудио файлы в формате mp3'
    DROPZONE_FILE_TOO_BIG = 'Вы можете загружать файлы не превышающие 20MB'
    DROPZONE_ENABLE_CSRF = True
    DROPZONE_MAX_FILES = 1,

    DROPZONE_IN_FORM = True,
    DROPZONE_UPLOAD_ON_CLICK = True,
    DROPZONE_UPLOAD_ACTION = 'upload_podcast_handle'  # URL or endpoint
    UNREGISTER_USER = 'Только зарегестрированные пользователи могу загружать подкасты'

