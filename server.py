'''
This module is server that checks emotions in given line.
'''
from flask import Flask
from flask import render_template
from flask import request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')


@app.route("/emotionDetector")
def emote_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detector()
        function. The output returned shows the emotions and its confidence 
        score for the provided text.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    check_anger_disgust_joy_none = response['anger'] is None and \
        response['disgust'] is None and \
        response['joy'] is None
    check_fear_sadness_dominant_none = response['fear'] is None and \
        response['sadness'] is None and \
        response['dominant_emotion'] is None

    if ( check_anger_disgust_joy_none and check_fear_sadness_dominant_none ):
        return 'Invalid Input! Please try again'
    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is 'anger': {response['anger']}, \
            'disgust': {response['disgust']}, 'fear': {response['fear']},\
            'joy': {response['joy']} and 'sadness': {response['sadness']}.\
             The dominant emotion is {response['dominant_emotion']}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
