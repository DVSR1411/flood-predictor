from flask import Flask, render_template, request
import os
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load('svmmodel.pkl')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        temp = request.form['cloudCover']
        Hum = request.form['annualRainfall']
        db = request.form['janFebRainfall']
        ap = request.form['marchMayRainfall']
        aal = request.form['juneSeptRainfall']
        data = [[float(temp), float(Hum), float(db), float(ap), float(aal)]]
        input_data = np.array(data)
        prediction = model.predict(input_data)
        res = True if prediction[0] > 0.5 else False
        result = f"The Prediction is: {res}"
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
