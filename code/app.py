# importing required libraries

from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn import metrics
import warnings
import pickle

warnings.filterwarnings("ignore")
from feature import FeatureExtraction

file = open("C:/phishing/Phishing-URL-Detection-master/pickle/model.pkl", "rb")
gbc = pickle.load(file)
file.close()


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1, 30)
        
        y_pred = gbc.predict(x)[0]
        # 1 is safe
        # -1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0, 0]
        y_pro_non_phishing = gbc.predict_proba(x)[0, 1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing * 100)
        print(pred)
        return render_template("index.html", xx=round(y_pro_non_phishing, 2), url=url)
    return render_template("index.html", xx=-1)

@app.route("/check_phishing", methods=["POST"])
def check_phishing():
    data = request.get_json()
    url = data.get("url")

    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1, 30)
    
    y_pred = gbc.predict(x)[0]
    y_pro_phishing = gbc.predict_proba(x)[0, 0]
    y_pro_non_phishing = gbc.predict_proba(x)[0, 1]

    # Convert boolean value to integer
    response = {
        "is_safe": int(y_pred == 1),
        "confidence": round(y_pro_non_phishing * 100, 2)
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
