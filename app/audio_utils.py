from pydub import AudioSegment
from gtts import gTTS
import os
from app import app


def text_to_speech(id_or_name, text):
    """
    check if dir for joke's and episode's files exists.
    takes text, makes Russian speech, saved into mp3 file
    """
    jokes_dir = os.path.join(app.config.get('STATIC_ROOT'), 'jokes')
    episodes_dir = os.path.join(app.config.get('STATIC_ROOT'), 'episodes')
    check_and_create_file_dir(jokes_dir, episodes_dir)

    if isinstance(id_or_name, int):  # TODO change to method and path from model (Jokes/Episode)
        file_name = os.path.join(
            app.config.get('STATIC_ROOT'), "jokes", f'{id_or_name}.mp3'
        )
    elif isinstance(id_or_name, str):
        file_name = os.path.join(
            app.config.get('STATIC_ROOT'), "episodes", f'{id_or_name}.mp3'
        )
    else:
        return

    tts = gTTS(text=text, lang='ru')
    tts.save(file_name)

    return file_name


def check_and_create_file_dir(jokes_dir, episodes_dir):
    """
    if file's directory doesn't exist, create it,
    else: pass
    """
    if not os.path.exists(jokes_dir):
        os.makedirs(jokes_dir)
    if not os.path.exists(episodes_dir):
        os.makedirs(episodes_dir)


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
