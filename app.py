import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from datetime import datetime

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on webpage
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('result.html', prediction_text='Bio gas Unit {}'.format(output))

@app.route('/dataset')
def data():
    return render_template('data.html')
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)