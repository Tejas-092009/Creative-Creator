from flask import Flask, render_template, request
import os

from utils.gemini_video import analyze_video
from utils.image_generator import generate_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "static/outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    video = request.files["video"]

    style = request.form["style"]

    filename = os.path.join(app.config["UPLOAD_FOLDER"], video.filename)

    video.save(filename)

    description = analyze_video(filename)

    image = generate_image(description, style)

    return render_template(
        "index.html",
        description=description,
        image=image
    )


if __name__ == "__main__":
    app.run(debug=True)
