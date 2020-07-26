from flask import Flask, render_template_string, request, jsonify
from model import *

app = Flask(__name__)
vect, model = loadModel()
emotionDB = {}

@app.route('/predict', methods=['POST'])
def doPredict():    
    text = [request.values.get('text', type = str)]
    name = [request.values.get('name', type=str)]
    print(nama, text)
    result = doPrediction(text, vect, model)
    
    try:
        emotionDB[name].append(result[0])
    except:
        emotionDB[name] = [result[0]]

    print(emotionDB[name])
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