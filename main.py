from flask import Flask, render_template_string, request, jsonify
from model import *

app = Flask(__name__)
vect, model = loadModel()

@app.route('/predict', methods=['POST'])
def doPredict():    
    text = [request.values.get('text', type = str)]
    print(text)
    result = doPrediction(text, vect, model)

    chat = {'chats': [
        {
            'text': 'Emosi anda saat ini : ' + result[0],
            'type': 'text'
        }
    ]}

    return jsonify(chat)

@app.route('/get', methods=['GET'])
def doGetStuff():
    text = [request.args.get('text', type = str)]
    result = doPrediction(text, vect, model)

    chat = {'chats': [
        {
            'text': 'Emosi anda saat ini : ' + result[0],
            'type': 'text'
        }
    ]}

    return jsonify(chat)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7010')