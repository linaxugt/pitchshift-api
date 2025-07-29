from flask import Flask, request, send_file
import librosa
import soundfile as sf
import tempfile

app = Flask(__name__)

@app.route('/shift_pitch', methods=['POST'])
def shift_pitch():
    audio = request.files.get("audio_file")
    n_steps = float(request.form.get("n_steps", 0))

    if not audio:
        return {"error": "No file received"}, 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_in:
        audio.save(temp_in.name)
        y, sr = librosa.load(temp_in.name, sr=None)
    
    y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=n_steps)

    temp_out_path = tempfile.mktemp(suffix=".wav")
    sf.write(temp_out_path, y_shifted, sr)

    return send_file(temp_out_path, mimetype="audio/wav", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
