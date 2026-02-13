from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application=Flask(__name__) ## creates an instance of flask which will be wsgi application
app=application

## import ridge regessor and standard scalar pickle
ridge_model=pickle.load(open('C:\\CP\\ML\\25 ML Project\\models\\ridge.pkl','rb'))
standard_scalar=pickle.load(open('C:\\CP\\ML\\25 ML Project\\models\\scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        
        new_data_scaled=standard_scalar.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)
        
        return render_template('home.html',results=result[0])
        
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)