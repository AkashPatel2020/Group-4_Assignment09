import requests
import random

def translate_text(text, source_lang, target_lang):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    headers = {
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "13efaf5087msh7753c93dc15c882p1452a2jsnf83ff2d2cfe3",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        data = response.json()
        translated_text = data['data']['translations'][0]['translatedText']
        return translated_text
    else:
        return "Translation failed with status code: {}".format(response.status_code)

if __name__ == "__main__":
    # List of English phrases
    english_phrases = [
        "Hello, how are you?",
        "What's your name?",
        "How's the weather today?",
        "I love learning new things.",
        "Where is the nearest restaurant?",
        "Can you help me with this?",
        "I am feeling happy today.",
        "What time is it?",
        "I want to travel the world.",
        "Do you speak English?"
    ]
    
    # Select a random English phrase
    random_phrase = random.choice(english_phrases)
    
    source_language = "en"  # English
    target_language = "de"  # German

    # Translate the random English phrase to German
    translated_text = translate_text(random_phrase, source_language, target_language)
    print("Random English Phrase:", random_phrase)
    print("Translated Text from English to German:", translated_text)