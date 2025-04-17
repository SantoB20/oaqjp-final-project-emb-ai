from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
from werkzeug.exceptions import HTTPException

app = Flask("Emotion Detection")

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def get_emotion_detector():
    text_to_analyze: str = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if "Error" in result:
        return 'An error acurred in the server', 500

    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.', 400
    
    return f"""
    For the given statement, the system response is 
    'anger': {result['anger']}, 
    'disgust': {result['disgust']}, 
    'fear': {result['fear']}, 
    'joy': {result['joy']} and 
    'sadness': {result['sadness']}. 
    The dominant emotion is {result['dominant_emotion']}.
    """, 200

@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return f'{error.name}: {error.description}. {error.code}', error.code

if __name__ == '__main__':
    app.run(debug=True, port=5500)