import pickle
from flask import Flask, render_template, request, jsonify, json
from numpy import empty
from model_files.ml_model import predict_cuisine

app = Flask("cuisine_prediction")

@app.route('/predict', methods=['POST'])
def predict():
    ingredients = request.form['ingredients']
    if ingredients=="":
        return json.dumps({'status':'OK','cuisine': 'none'});
    with open('./model_files/model.bin', 'rb') as f_in:
        model=pickle.load(f_in)
        f_in.close()
    
    prediction=predict_cuisine(ingredients, model)[0]
    return json.dumps({'status':'OK','cuisine': prediction});

@app.route('/', methods=['GET'])
def Home():
   return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
