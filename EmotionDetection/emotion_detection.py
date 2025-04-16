import json
import requests

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = { "raw_document": { "text": text_to_analyze } }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(URL, json = myobj, headers = header, timeout = 10)

    if response.status_code == 400:
        emotions = { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
        return emotions
    formatted_response = json.loads(response.text)
    
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = None
    for key in emotions.keys():
        if dominant_emotion is None:
            dominant_emotion = key
        else:
            if emotions[dominant_emotion] < emotions[key]:
                dominant_emotion = key
    
    emotions['dominant_emotion'] = dominant_emotion

    return emotions