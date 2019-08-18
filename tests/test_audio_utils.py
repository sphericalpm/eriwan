from app.audio_utils import (
    text_to_speech,
    check_and_create_file_dir,
    concatenate_audios
)

def test_text_to_speech():
    pass
    with open(abs_graph_path, 'rb') as f1, \
        open(abs_test_graph_path, 'rb') as f2:
            while True:
            b1, b2 = f1.read(1), f2.read(1)
            if not b1 or not b2:
                break
            i = struct.unpack('B', b1)[0] - struct.unpack('B', b2)[0]

            assert i == 0


def check_and_create_file_dir():
    pass


def concatenate_audios():
    pass
