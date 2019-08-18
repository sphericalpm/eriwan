
if __name__ == "__main__":
    from app.audio_utils import text_to_speech, concatenate_audios
    speech = text_to_speech("Всем привет")
    concatenate_audios(
        ["static/jingles/jingle.mp3", speech, "static/jingles/jingle.mp3"],
        "episode",
        "3")
