import os.path as path
import os
import struct

from app.audio_utils import (
    text_to_speech,
    concatenate_audios
)


def test_text_to_speech():
    speech_path = text_to_speech("Всем привет")

    script_path = path.abspath(path.join(os.getcwd()))
    test_audio_path = os.path.join(
        script_path,
        "tests",
        "test_data",
        'test_audio.mp3'
    )

    with open(speech_path, 'rb') as f1, \
        open(test_audio_path, 'rb') as f2:

        while True:
            b1, b2 = f1.read(1), f2.read(1)
            if not b1 or not b2:
                break
            i = struct.unpack('B', b1)[0] - struct.unpack('B', b2)[0]

            assert i == 0


def test_concatenate_audios():
    script_path = path.abspath(path.join(os.getcwd()))
    test_audio_path = os.path.join(
        script_path,
        "tests",
        "test_data",
        'test_audio_with_jingle.mp3'
    )

    concatenate_audio_path = os.path.join(
        script_path,
        "tests",
        "test_data",
        "jingle_and_joke.mp3"
        )
    voice_from_text = text_to_speech("Всем привет")
    jingle = "app/static/jingles/jingle.mp3"

    concatenate_audios(
        [jingle, voice_from_text, jingle],
        concatenate_audio_path
    )

    with open(concatenate_audio_path, 'rb') as f1, \
        open(test_audio_path, 'rb') as f2:

        while True:
            b1, b2 = f1.read(1), f2.read(1)
            if not b1 or not b2:
                break
            i = struct.unpack('B', b1)[0] - struct.unpack('B', b2)[0]

            assert i == 0
