import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model_numpy.pkl", "rb"))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    feature = [np.array(float_features)]
    prediction = model.predict(feature)[0]

    if prediction == 0:
        prediction_text = "Anda tidak memiliki riwayat penyakit jantung"
    else:
        prediction_text = "Anda memiliki riwayat penyakit jantung"

    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
