from pydub import AudioSegment
from gtts import gTTS
import tempfile


def text_to_speech(text):
    """
    takes text, makes Russian speech, saved into temporary mp3 file
    """
    temporary_file = tempfile.NamedTemporaryFile(suffix=".mp3")
    tts = gTTS(text=text, lang='ru')
    tts.save(temporary_file.name)

    return temporary_file


def concatenate_audios(file_list, out_path):
    """
    Concatenate audios into one file
    :param out_path: path for saving mp3 file or file itself
    :param file_list: audio path list
    :return:
    """

    res = AudioSegment.empty()
    for audio_path in file_list:
        res += AudioSegment.from_mp3(audio_path)
    res.export(out_path, format='mp3')


def prepend_intro_text_and_save(audio_file, intro_text, output_path):
    intro_audio = AudioSegment.from_mp3(text_to_speech(intro_text))
    base_audio = AudioSegment.from_mp3(audio_file)
    result = intro_audio + base_audio
    result.export(output_path, format='mp3')
