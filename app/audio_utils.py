from pydub import AudioSegment
from gtts import gTTS
import tempfile


def text_to_speech(text):
    """
    takes text, makes Russian speech, saved into temporary mp3 file
    """
    temporary_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tts = gTTS(text=text, lang='ru')
    tts.save(temporary_file.name)

    return temporary_file.name


def concatenate_audios(path_list, out_path):
    """
    Concatenate audios into one file
    :param out_path: path for saving mp3 file
    :param path_list: audio path list
    :return:
    """

    res = AudioSegment.empty()
    for audio_path in path_list:
        res += AudioSegment.from_mp3(audio_path)
    res.export(out_path, format='mp3')