import os
import subprocess
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from rembg import remove

app = Flask(__name__)
CORS(app)  # allow frontend to connect

# Path to Real-ESRGAN
ESRGAN_PATH = r"C:\Users\HP\Downloads\RealESRGAN-ncnn-vulkan-20220424-windows\realesrgan-ncnn-vulkan.exe"

# -------- ENHANCE IMAGE --------
@app.route("/enhance", methods=["POST"])
def enhance_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    input_path = "input.png"
    output_path = "enhanced.png"
    file.save(input_path)

    if not os.path.exists(ESRGAN_PATH):
        return jsonify({"error": "Real-ESRGAN not found!"}), 500

    try:
        subprocess.run([ESRGAN_PATH, "-i", input_path, "-o", output_path])
        return send_file(output_path, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------- REMOVE BACKGROUND --------
@app.route("/remove_bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    input_data = file.read()
    output_data = remove(input_data)

    output_path = "no_bg.png"
    with open(output_path, "wb") as f:
        f.write(output_data)

    return send_file(output_path, mimetype="image/png")


@app.route("/")
def home():
    return "✅ Flask backend is running!"


if __name__ == "__main__":
    app.run(debug=True)
