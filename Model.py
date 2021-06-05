import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from prepocess import filter_data
from finding_mean import similarity
from text_classification import classified_topic
from topic_modeling import modeled_topic

import time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        extension = ".txt"
        file_name = timestr + extension
        file.save(os.path.join('uploads', file_name))
        return redirect(url_for('prediction', filename=file_name))
    return render_template('index.html')


@app.route('/prediction/<filename>')
def prediction(filename):
    threshold = [0.08879327017206416,
                 0.05345086075824122,
                 0.08716082301678847,
                 0.11631393924306697,
                 0.09086767645786813]
    directory = "Dataset\Train"
    if_similarity = similarity(filename, directory, threshold)
    if if_similarity == True:
        topic = classified_topic(filename)
    else:
        topic = modeled_topic(filename)
    return render_template('predict.html', predictions=topic)


if __name__ == "__main__":
    app.run(debug=True)
