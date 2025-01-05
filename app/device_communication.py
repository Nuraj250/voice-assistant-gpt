from flask import Flask, request

app = Flask(__name__)

@app.route('/audio', methods=['POST'])
def receive_audio():
    audio_data = request.files['audio']
    # Save or process the audio file
    return "Audio received!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
