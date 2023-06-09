"""
App File
--------
"""
from flask import Flask, request, render_template
import os
import pickle
import random
import pickle

# Load the logistic regression model
with open('C:\Users\ALLADI ASHWIK RAO\OneDrive\Desktop\flask\model.pkl', 'rb') as file:
    logistic = pickle.load(file)
    randomforest = pickle.load(file)
    svm_model=pickle.load(file)
path = os.getcwd()



def get_predictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, req_model):
    mylist = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    if req_model == 'Logistic':
        print(req_model)
        return logistic.predict(vals)[0]

    elif req_model == 'RandomForest':
        # print(req_model)
        return randomforest.predict(vals)[0]

    elif req_model == 'SVM':
        # print(req_model)
        return svm_model.predict(vals)[0]
    else:
        return "Cannot Predict"


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['Age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']

        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']

        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']

        req_model = request.form['req_model']

        target = get_predictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                                 exang, oldpeak, slope, ca, thal, req_model)
        target=random.randint(0,92)

        if (target>=30):
            sale_making = 'Potential heart disease detected .. Go see a doctor'
        else:
            sale_making = 'unlikely to have a heart disease .. keep exercising'

        return render_template('home.html', target=target, sale_making=sale_making)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
