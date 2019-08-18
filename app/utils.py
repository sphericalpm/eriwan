from functools import wraps
from pydub import AudioSegment

from flask import request, redirect, url_for, flash
from flask_login import current_user


def concatenate_audios(path_list, out_path):
    """
    Concatenate audios into one file
    :param out_path: path to result mp3
    :param path_list: audio path list
    :return:
    """
    res = AudioSegment.empty()
    for audio_path in path_list:
        res += AudioSegment.from_mp3(audio_path)
    res.export(out_path, format='mp3')


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if not current_user.is_admin:
                flash("Для доступа нужно обладать правами администратора")
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return redirect(url_for('login'))
    return decorated_function
