from flask import Flask, render_template, request,jsonify
import numpy as np
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = pickle.load(open('Kidney.pkl', 'rb'))

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        content=request.json
        sg=float(content["sg"])
        htn=float(content["htn"])
        hemo=float(content["hemo"])
        dm=float(content["dm"])
        al=float(content["al"])
        appet=float(content["appet"])
        rc=float(content["rc"])
        pc=float(content["pc"])

        values = np.array([[sg, htn, hemo, dm, al, appet, rc, pc]])
        prediction = model.predict(values)
        return jsonify(result=str(prediction[0]), id=200)

if __name__ == "__main__":
    app.run(debug=True)
