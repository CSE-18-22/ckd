from flask import Flask, render_template, request,jsonify
import numpy as np
import pickle
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
model = pickle.load(open('Kidney.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        content=request.json
        # sg = float(request.form['sg'])
        # htn = float(request.form['htn'])
        # hemo = float(request.form['hemo'])
        # dm = float(request.form['dm'])
        # al = float(request.form['al'])
        # appet = float(request.form['appet'])
        # rc = float(request.form['rc'])
        # pc = float(request.form['pc'])
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

        # return render_template('result.html', prediction=prediction)
        # return json.dumps(True)
        return jsonify(result=True, id=200)

if __name__ == "__main__":
    app.run(debug=True)

