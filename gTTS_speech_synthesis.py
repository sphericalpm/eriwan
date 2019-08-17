from gtts import gTTS

def text_to_speech(text):
    """
    takes text, makes Russian speech
    """
    tts = gTTS(text=text, lang='ru')
    file_name = "hello1.mp3"
    tts.save(file_name)

    return file

if __name__ == "__main__":
    #text = "Армянская семья так любила извиняться, что взяла фамилию Сорян."
    text = "Рыла свинья белорыла, тупорыла; полдвора рылом изрыла, вырыла, подрыла"
    print(text_to_speech(text))
