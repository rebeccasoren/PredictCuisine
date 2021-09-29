import pickle
from flask import Flask, render_template, request, jsonify
from model_files.ml_model import predict_cuisine

app = Flask("cuisine_prediction")

@app.route('/', methods=['POST'])
def predict():
    recipe=request.get_json()
    with open('./model_files/model.bin', 'rb') as f_in:
        model=pickle.load(f_in)
        f_in.close()
    
    predictions=predict_cuisine(recipe, model)

    response={
        'predictions': list(predictions)
    }

    return jsonify(response)


@app.route('/', methods=['GET'])
def Home():
   return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
