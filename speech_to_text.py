
import whisper
import tempfile

model = whisper.load_model("base")

def speech_to_text(audio_bytes):
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp.flush()
        result = model.transcribe(tmp.name)
    return result["text"]
