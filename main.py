from flask import Flask, render_template_string, request
from model import *

app = Flask(__name__)
vect, model = loadModel()

@app.route('/predict', methods=['POST'])
def doPredict():    
    text = [request.values.get('text', type = str)]
    print(text)
    result = doPrediction(text, vect, model)
    return result[0]

@app.route('/get', methods=['GET'])
def doGetStuff():
    text = [request.args.get('text', type = str)]
    result = doPrediction(text, vect, model)
    return result[0]

if __name__ == '__main__':
    app.run(debug=True)