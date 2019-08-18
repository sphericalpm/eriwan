from pydub import AudioSegment
from gtts import gTTS
import os
import tempfile

from app import app


def text_to_speech(text):
    """
    takes text, makes Russian speech, saved into temporary mp3 file
    """
    temporary_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts = gTTS(text=text, lang='ru')
    tts.save(temporary_file.name)

    return temporary_file.name


def check_and_create_file_dir(directory):
    """
    if file's directory doesn't exist, create it,
    else: pass
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory


def concatenate_audios(path_list, folder_name, id):
    """
    Concatenate audios into one file
    :param out_path: path to result mp3
    :param path_list: audio path list
    :return:
    """
    directory = os.path.join(app.config.get('MEDIA_ROOT'), folder_name)
    out_path = os.path.join(check_and_create_file_dir(directory), f'{id}.mp3')

    res = AudioSegment.empty()
    for audio_path in path_list:
        res += AudioSegment.from_mp3(audio_path)
    res.export(out_path, format='mp3')



