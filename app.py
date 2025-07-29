from flask import Flask, request, send_file
import tempfile
import librosa
import soundfile as sf
import os

app = Flask(__name__)

@app.route('/shift_pitch', methods=['POST'])
def shift_pitch():
    if 'audio_file' not in request.files or 'n_steps' not in request.form:
        return "Missing file or pitch shift parameter", 400

    audio_file = request.files['audio_file']
    n_steps = float(request.form['n_steps'])

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.wav")
        output_path = os.path.join(tmpdir, "output.wav")
       
        # 保存上传的文件
        audio_file.save(input_path)

        # 加载音频
        y, sr = librosa.load(input_path, sr=None)
       
        # 变调
        y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=n_steps)

        # 保存变调后的音频
        sf.write(output_path, y_shifted, sr)

        return send_file(output_path, mimetype="audio/wav", as_attachment=True, download_name="shifted.wav")

@app.route('/')
def home():
    return "Pitch Shift API is running!"
