import os

from flask import Flask, render_template, url_for, redirect, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'C:\\Users\\nikhi\\Desktop\\HackNotts\\videosum\\frontend\\File'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/transcribe", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['FileName']
        filename = secure_filename(file.filename)
        #file.save(app.config['UPLOAD_FOLDER'], filename)
        return render_template('transcribe.html')


if __name__ == "__main__":
    app.run(port=4996, debug=True)
