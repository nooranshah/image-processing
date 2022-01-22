
from flask import render_template, request
from flask import redirect, url_for
from PIL import Image

import os

UPLOAD_FOLDER = "static/uploads"


def base():
    return render_template("base.html")


def index():
    return render_template("index.html")


def faceapp():
    return render_template("faceapp.html")


def getWidth(path):

    img = Image.open(path)
    size = img.size  # width and height
    aspect = size[0]/size[1]  # width/height
    w = 300 * aspect
    return int(w)


def gender():
    if request.method == 'POST':
        f = request.files['image']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)
        # processing

        w = getWidth(path)
        return render_template("gender.html", fileupload=True, img_name=filename, w=w)

    return render_template("gender.html", fileupload=False, img_name='freeai.png', w="300")
