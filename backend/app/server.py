import os
from tempfile import gettempdir

from app.audio import get_wav
from flask import Flask, jsonify, request
from app.speech import get_transcript
from app.summariser import summarise_transcript
from summarizer import Summarizer
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["UPLOAD_FOLDER"] = gettempdir()
app.config["UPLOAD_EXTENSIONS"] = [".mp4", ".mov", ".avi", ".m4v", ".mkv"]


@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    ratio = request.form["ratio"]
    if uploaded_file.filename is None:
        return jsonify(message="Filename is missing"), 400
    filename = secure_filename(uploaded_file.filename)
    file_ext = os.path.splitext(filename)[1]
    if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
        return jsonify(message="File is the wrong format"), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    uploaded_file.save(file_path)

    wav_file = get_wav(file_path)
    transcript = get_transcript(str(wav_file))
    sum_transcript = summarise_transcript(Summarizer(), transcript, ratio=float(ratio))

    return jsonify(main=transcript, summarized=sum_transcript), 200


if __name__ == "__main__":
    app.run(port=4996, debug=True)
