# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:55:43 2020

@author: lenovo
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#from joblib import load
app = Flask(__name__)
model = pickle.load(open('project1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[int(x) for x in request.form.values()]]
    #test = [np.array(x_test)]
    print(x_test)
     
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if output==0:
        pred = "YOU ARE PERFECTLY ALRIGHT"
    elif output==1:
        pred="NEED TO TAKE CARE OF YOUR HEALTH "
    else :
        pred = "NEED CONSULTATION"
    return render_template('index.html', prediction_text=' {}'.format(pred))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)




if __name__ == "__main__":
    app.run(debug=True)
