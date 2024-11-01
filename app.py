from flask import Flask, render_template, request, redirect, url_for, send_file
from filters import apply_filter
import os
import cv2
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'


# Ana sayfa rotası
@app.route('/')
def index():
    return render_template('index.html')


# Fotoğraf yükleme ve işleme rotası
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(url_for('index'))

    file = request.files['image']
    if file.filename == '':
        return redirect(url_for('index'))

    # Görüntüyü yükle ve filtre uygula
    filter_name = request.form['filter']
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    processed_image = apply_filter(filepath, filter_name)
    processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], "processed_" + filename)
    cv2.imwrite(processed_filepath, processed_image)

    return send_file(processed_filepath, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
