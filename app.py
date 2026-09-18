from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)

model = tf.keras.models.load_model("Face-mask-detection.keras")

classes = {
    0: "With Mask",
    1: "Without Mask"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["image"]

        image_data = base64.b64decode(data.split(",")[1])
        image = Image.open(io.BytesIO(image_data)).convert("RGB")

        image = image.resize((160, 160))

        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array, verbose=0)

        if prediction.shape[-1] == 1:
            result = 1 if prediction[0][0] >= 0.5 else 0
            confidence = prediction[0][0] if result == 1 else 1 - prediction[0][0]
        else:
            result = np.argmax(prediction[0])
            confidence = prediction[0][result]

        return jsonify({
            "prediction": classes[result],
            "confidence": float(confidence * 100)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)