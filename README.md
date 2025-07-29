# PitchShift API

This is a simple Flask API that allows you to upload a `.wav` file and shift its pitch by a number of semitones using Librosa.

## How to deploy (e.g. on Render)
1. Upload this folder to a GitHub repo
2. Create a new Web Service on Render
3. Use the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`

API Endpoint: `/shift_pitch` (POST)
- Params: 
  - `audio_file` (File, required)
  - `n_steps` (float, optional, default = 0)
