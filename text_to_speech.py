
from gtts import gTTS
import io

def text_to_speech(text):
    tts = gTTS(text)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    return mp3_fp.getvalue()
