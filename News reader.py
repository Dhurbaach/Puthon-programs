def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json
    speak("News for today lets began")
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=9ef1bc09606a4a73a18786b24a6af89d')

    news = requests.get(url).text
    news__dict=json.loads(news)
    print(news__dict["articles"])
    arts=news__dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news")