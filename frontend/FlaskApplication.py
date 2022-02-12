import os

from flask import Flask, render_template, url_for, redirect, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/index", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html')
        file = request.files['file']

        if file.filename == '':
            return render_template('index.html')

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('index.html')


if __name__ == "__main__":
    app.run(port=4996)
