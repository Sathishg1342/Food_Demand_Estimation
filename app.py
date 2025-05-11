# import the necessary packages
import pandas as pd
import numpy as np
import pickle,database
import os
from flask import Flask,request, render_template
app=Flask(__name__,template_folder="Templates")
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')
@app.route('/home', methods=['GET'])
def about():
    return render_template('home.html')
@app.route('/pred',methods=['GET'])
def page():
    return render_template('upload.html',prediction_text='')
@app.route('/submit',methods=['GET','POST'])
def submit():
    fd=[x for x in request.form.values()]
    if(database.insert_into_db(fd[0],fd[1],fd[2])):
        return '<html><body><script>alert("Feedback Accpted.");' \
           'location.replace("home");</script></body></html>'
    else:return '<html><body><script>alert("Submit the feedback again.");' \
                'location.replace("feedback");</script></body></html>'
@app.route('/feedback',methods=['GET','POST'])
def feedback():
    return render_template('Feedback.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    model = pickle.load(open('fdemand.pkl', 'rb'))
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    features_name = ['homepage_featured', 'emailer_for_promotion', 'op_area', 'cuisine','city_code', 'region_code', 'category']
    prediction = model.predict(features_value)
    output=int(prediction[0])
    return render_template('upload.html', prediction_text='Number of orders:'+str(output)+"(Aprox..)")
if __name__ == '__main__':
      app.run(debug=True,port=8000)
