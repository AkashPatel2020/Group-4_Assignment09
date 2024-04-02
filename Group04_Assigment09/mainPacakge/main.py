# main.py 
import requests
import json

if __name__ =="__main__":
    
    def translate_text(text, source_lang, target_lang):
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
        headers = {
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": "ac38db332emsh019d1632ab66393p1d1734jsn1cb0729b4fa4",
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
        text_to_translate = "Hello, how are you?"
        source_language = "en"  # English
        target_language = "es"  # Spanish
        translated_text = translate_text(text_to_translate, source_language, target_language)
        print("Translated Text:", translated_text)