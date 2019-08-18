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


# create_graph(arm_list)

#     script_path = path.abspath(path.join(os.getcwd()))
#     graph_path = "Right arm_graph.png"
#     test_graph_path = "test_graph.png"

#     abs_graph_path = os.path.join(script_path, graph_path)
#     abs_test_graph_path = os.path.join(script_path, test_graph_path)

#     with open(abs_graph_path, 'rb') as f1, \
#         open(abs_test_graph_path, 'rb') as f2:

#         while True:
#             b1, b2 = f1.read(1), f2.read(1)
#             if not b1 or not b2:
#                 break
#             i = struct.unpack('B', b1)[0] - struct.unpack('B', b2)[0]

#             assert i == 0

#     with pytest.raises(IndexError) as error:
#         assert create_graph([]) in str(error.value)

#     with pytest.raises(KeyError) as error:
#         assert create_graph({}) in str(error.value)

#     with pytest.raises(ValueError) as error:
#         assert create_graph(arm_list_v2) in str(error.value)
