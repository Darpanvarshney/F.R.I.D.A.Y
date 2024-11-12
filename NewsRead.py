import pyttsx3
from newsapi import NewsApiClient

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    newsapi = NewsApiClient(api_key='enter you api key ')
    top_headlines = newsapi.get_top_headlines(q=None,
                                          sources=None,
                                          category=None,
                                          language=None,
                                          country='in',
                                            page_size=10)
    arts = top_headlines["articles"]
    speak("top 10 news in india are ,")
    for articles in arts :
        article = articles["title"]

        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        
    speak("thats all")
