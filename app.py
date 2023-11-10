import numpy as np
import pandas as pd
from flask import Flask, request, render_template

import pickle

app = Flask(__name__)

import model

database = {'sai':'sai', 'ajay':'ajay', 'madhu':'madhu', 'avilash':'avilash'}

@app.route('/login', methods=['POST','GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['userpassword']
    if name1 not in database:
        return render_template('home.html', info='invalid user')
    else:
        if database[name1] != pwd:
            return render_template('home.html', info='invalid password')
        else:
            return render_template('index.html', text=name1)

@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin', methods=['POST','GET'])
def checkLogin():
    user = request.form['auser']
    pwd = request.form['apass']
    if user == "admin" and pwd == "admin":
        return render_template('admin.html', name=user)
    else:
        return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    
    
    input_features = [x for x in request.form.values()]
    age = input_features[0]
    sex = input_features[1]
    on_thyroxine = input_features[2]
    sick = input_features[3]
    thyroid_surgery = input_features[4]
    I131_treatment = input_features[5]
    query_hypothyroid = input_features[6]
    query_hyperthyroid = input_features[7]
    goitre = input_features[8]
    TSH = input_features[9]
    T3 = input_features[10]
    TT4 = input_features[11]
    T4U = input_features[12]
    FTI = input_features[13]
    
    predicted = model.predict_output(age, sex, on_thyroxine, sick, thyroid_surgery, I131_treatment, query_hypothyroid, query_hyperthyroid, goitre, TSH, T3, TT4, T4U, FTI)
    
    if predicted == 0:
        x = "The person does not have any thyroid disease"

    else:
        x = "The person have the throid disease"

    return render_template('index.html', prediction_text = x, t = TSH)
                           
if __name__ == "__main__":
    app.run(debug=True)
                           