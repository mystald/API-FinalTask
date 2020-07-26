from flask import Flask, render_template_string, request, jsonify
from model import *

app = Flask(__name__)
vect, model = loadModel()
emotionDB = {}

@app.route('/predict', methods=['POST'])
def doPredict():    
    text = [request.values.get('text', type = str)]
    name = request.values.get('name', type=str)
    print(name, text)
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
        },
        {
            'variable':{
                'currentEmotion': result[0]
            },
            'type': 'variable'
        }
    ]}

    return jsonify(chat)

@app.route('/history', methods=['GET'])
def showHistory():
    name = request.values.get('name', type=str)
    chats = {'chats': []}
    if name in emotionDB:
        chats['chats'].append(
            {
                'text': "Nama : " + name,
                'type': 'text'
            }
        )
        for emotion in emotionDB[name]:
            chats['chats'].append(
                {
                    'text': emotion,
                    'type': 'text'
                }
            )
    else:
        chats['chats'].append(
            {
                'text': "Anda belum memasukkan update apapun",
                'type': 'text'
            }
        )
    return jsonify(chats)

@app.route('/status', methods=['GET'])
def showCurrentStatus():
    name = request.values.get('name', type=str)
    chats = {'chats': []}
    if name in emotionDB:
        chats['chats'].append(
            {
                'text': "Nama : " + name,
                'type': 'text'
            }
        )

        emotion = emotionDB[name][-1]
        chats['chats'].append(
            {
                'text': 'Emotion saat ini : ' + emotion,
                'type': 'text'
            }
        )
    else:
        chats['chats'].append(
            {
                'text': "Anda belum memasukkan update apapun",
                'type': 'text'
            }
        )
    return jsonify(chats)

@app.route('/', methods=['GET'])
def doGetStuff():
    #text = [request.args.get('text', type = str)]
    #result = doPrediction(text, vect, model)

    #chat = {'chats': [
    #    {
    #        'text': 'Emosi anda saat ini : ' + result[0],
    #        'type': 'text'
    #    }
    #]}

    return "IT WORKS!!1!1!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7010')
