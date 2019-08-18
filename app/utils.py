from pydub import AudioSegment


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
