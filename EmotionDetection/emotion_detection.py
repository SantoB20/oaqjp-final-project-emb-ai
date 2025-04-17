import requests
from requests import Response
from pprint import pprint

def emotion_detector(text_to_analyze: str) -> str | dict:
    if text_to_analyze is None or text_to_analyze == '' or text_to_analyze == ' ':
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }

    url: str = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers: dict = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    data: dict = {'raw_document': {'text': text_to_analyze}}
    
    res: Response = requests.post(url, headers=headers, json=data)
    if res.ok:
        scores: dict = res.json()['emotionPredictions'][0]['emotion']
        dominant_emotion = max(scores, key=scores.get)
        scores['dominant_emotion'] = dominant_emotion
        return scores
    return f"Error: {res.status_code}, {res.text}"

def main():
    pprint(emotion_detector('I am so happy I am doing this.'))

if __name__ == '__main__':
    main()