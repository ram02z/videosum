import os

from flask import Flask, render_template, url_for, redirect, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/transcribe", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['FileName']
        return render_template('transcribe.html')


if __name__ == "__main__":
    app.run(port=4996, debug=True)
