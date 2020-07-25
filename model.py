import pickle

def loadModel():
    vect = pickle.load(open("isear_tfidf1.pkl", 'rb'))
    model = pickle.load(open('isear_model.sav', 'rb'))
    return vect, model

def doPrediction(text, vect, model):
    text_vected = vect.transform(text)
    pred_result = model.predict(text_vected)
    return pred_result