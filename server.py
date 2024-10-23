"""
Flask web server for emotion detection.

Provides two endpoints:
1. `/emotionDetector`: Detects emotions from input text.
2. `/`: Renders the homepage.

Runs on host '0.0.0.0' and port 5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    """
    Detects emotions from input text.

    Retrieves text from the 'textToAnalyze' query parameter, passes it to the emotion detector, 
    and returns a formatted response with detected emotions and the dominant emotion.

    Returns:
        str: Formatted response with emotions or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyze)
    if resp is None:
        return 'Invalid text! Please try again!'

    r = [f"'{key}': {value:.9f}" for key, value in resp.items() if key != "dom_emo"]
    d_emo = resp['dom_emo']
    return f"For the given statement, the system response is {', '.join(resp_list)}. The dominant emotion is {d_emo}."


@app.route("/")
def render_index_page():
    """
    Renders the homepage.
    Returns:
        HTML: Rendered index.html page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
