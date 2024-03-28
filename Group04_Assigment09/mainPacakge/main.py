# main.py 
import requests
import json

if __name__ =="__main__":
    
    
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"
    
    headers = {
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "ac38db332emsh019d1632ab66393p1d1734jsn1cb0729b4fa4",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    languages = data['data']['languages']
    
    # Filter languages starting with the letter 'A'
    filtered_languages = [lang['language'] for lang in languages if lang['language'].lower().startswith('a')]
    
    print("Languages starting with 'A':", filtered_languages)