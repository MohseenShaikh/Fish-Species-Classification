
import numpy as np
import pickle

from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

scaler_in = open("scaler.pkl", 'rb')
scaler = pickle.load(scaler_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict_fish():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    final_features = scaler.fit_transform(final_features)
    prediction = classifier.predict(final_features)

    
    return render_template('index.html', prediction_text='The fish belong to species {}'.format(prediction[0]))
    
    


if __name__=='__main__':
    app.run()