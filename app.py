from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("saved_models/savedmodel.pth")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    img = Image.open(file).convert("L")
    img = img.resize((64, 64))

    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = img_array.flatten().reshape(1, -1)

    prediction = model.predict(img_array)

    return render_template(
        "index.html",
        prediction=f"Person ID: {prediction[0]}"
    )

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)