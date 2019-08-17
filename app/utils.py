from pydub import AudioSegment
from gtts import gTTS
import os


def text_to_speech(id_or_name, text):
    """
    check if dir for joke's and episode's files exists.
    takes text, makes Russian speech, saved into mp3 file
    """
    current_dir = os.getcwd()
    jokes_dir = ("%s/%s") % (current_dir, "jokes")
    episodes_dir = ("%s/%s") % (current_dir, "episodes")
    check_and_create_file_dir(jokes_dir, episodes_dir)

    if isinstance(id_or_name, int):
        file_name = "%s/%s.mp3" % (jokes_dir, id_or_name)

    elif isinstance(id_or_name, str):
        file_name = "%s/%s.mp3" % (episodes_dir, id_or_name)

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

if __name__ == "__main__":
    text = "Армянская семья так любила извиняться, что взяла фамилию Сорян."
    id = "name"
    file_path = text_to_speech(id, text)
    print(file_path)
    concatenate_audios(['static/jingles/jingle.mp3', file_path, 'static/jingles/jingle.mp3'], file_path)
