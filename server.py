from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detetion_action():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    emotions = ''.join([f"'{key}': {value}, " for key, value in response.items()])

    return "For the given statement, the system response is {} The dominant emotion is <b>{}</b>.".format(emotions, response['dominant_emotion'])

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)