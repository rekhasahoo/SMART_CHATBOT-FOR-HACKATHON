
from flask import Flask, request, jsonify
from speech_to_text import speech_to_text
from chatbot import generate_response
from text_to_speech import text_to_speech
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    audio_data = request.files["audio"]
    audio_bytes = audio_data.read()
    
    text = speech_to_text(audio_bytes)
    response_text = generate_response(text)
    audio_response = text_to_speech(response_text)
    
    audio_base64 = base64.b64encode(audio_response).decode("utf-8")
    
    return jsonify({"response": response_text, "audio": audio_base64})

if __name__ == "__main__":
    app.run(debug=True)
