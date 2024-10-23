import requests  # Import the requests library to handle HTTP requests
import json # Import the json library


def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    # URL of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }  
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header) 
    # convert response to a dict using json
    formatted_response = json.loads(response.text)
    # Logic for error handling
    if response.status_code == 200:
        # Extract the emotions
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        # Logic to find the dominant emotion with the highest score
        dom_emo = max(emotions, key = emotions.get)
        # Add the dominant emotion to the dict
        emotions['dominant_emotion'] = dominant_emotion
    
    elif response.status_code == 400:
        emotions = None
    
    return emotions  # Return the response as the instruction