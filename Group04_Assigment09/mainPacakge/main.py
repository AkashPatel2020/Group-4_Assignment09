# main.py
# Name: Leonie Troeger, Akash Patel
# email: troegele@mail.uc.edu, Patel5a5@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/04/2024
# Course/Section: IS 4010 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Using Google Translator API and written python code to translate random class and book facts 
# Citations: https://rapidapi.com/googlecloud/api/google-translate1, https://medium.com/analytics-vidhya/how-to-translate-text-with-python-9d203139dcf5, https://www.google.com/books/edition/Introduction_to_JavaScript_Object_Notati/Qv9PCgAAQBAJ?hl=en&gbpv=1 
# Anything else that's relevant: 

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
        return "The translation from English to German failed with status code: {}".format(response.status_code)

if __name__ == "__main__":
    # List of random facts from class
    english_ClassFacts = [
        "JSON data is a python dictionary",
        "API means Application Programming Interface",
        "A data interchange format is a text used to exchange data between platforms.",
        "JSON is based JavaScript object literals",
        "In the real world, there are hundreds of programming langauges"
    ]
    
    # Select a random English phrase
    random_facts = random.choice(english_ClassFacts)
    
    source_language = "en"  # English
    target_language = "de"  # German

    # Translate the random English phrase to German
    translated_text = translate_text(random_facts, source_language, target_language)
    print("Random facts in English:", random_facts)
    print("Translated Text to German:", translated_text)