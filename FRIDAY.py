import os
import pyautogui
from email.mime import audio
from pyautogui import sleep
import pyttsx3
import pywhatkit.sc
import speech_recognition as sr
import datetime
import webbrowser as wb
import wikipedia
import pywhatkit
import requests
from googletrans import Translator
from bs4 import BeautifulSoup
import random
import wikipedia as googleScrap
import json 
import pickle 
import numpy as np 
import nltk 
from nltk.stem import WordNetLemmatizer
from keras.models import load_model # type: ignore
from calu import calu
from pygame import mixer
from plyer import notification
import healthadviser
import image_generator

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())

words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))
model = load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break 
    return result 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voicespeed = 150
engine.setProperty('rate', voicespeed)

 #audio pass
def speak(audio) :  
  engine.say(audio)
  engine.runAndWait()

# wish me
def wishMe():
 engine.say(audio)
 engine.runAndWait()

 hour = int(datetime.datetime.now().hour)
 if hour >= 0 and hour < 12:
    speak("good morning sir")
    sleep(0.5) 
    
 elif hour >= 12 and hour < 18:
    speak("good afternoon sir")
    sleep(0.5)
    
 else:
  speak("good evening sir") 
  sleep(0.5)
  
def Takecommand ():               
  r = sr.Recognizer()
  with sr.Microphone () as source:   
    print("Listening...")
    r.pause_threshold = 1
    r.energy_threshold = 1000
    audio = r.listen(source)
  
  try:
      print("reccognizing ...")
      query = r.recognize_google(audio , language='hi')
     
  except BaseException as e: 
    print("say that again plz ...")
    return "none"  
  return query

def eng_hi(text):
  line = str(text)
  translate_e = Translator()
  result = translate_e.translate(line)
  data = result.text
  print(f"you : {data}")
  return data

def connect():
  query = Takecommand()
  data  = eng_hi(query)
  return data

wishMe()
while True:
  Start = connect().lower()
  if 'friday' in Start:
      query = Start

      if 'wikipedia' in query :
        speak('searching on wikipedia ...')
        query = query.replace("wikipedia" , "")
        query = query.replace("search on" , "")
        query = query.replace("friday" , "")
        try:
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)  
        except:
          speak("sorry i am unable to find")

      elif "google" in query:
        query = query.replace("friday","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")    

      if 'coding' in query or 'code' in query:
            speak("ok give me time I am running your command")
            pyautogui.press("super")
            pyautogui.typewrite("chrome")
            sleep(0.5)
            pyautogui.press("enter")
            sleep(0.5)
            pyautogui.press("super")
            pyautogui.typewrite("vs code")
            sleep(0.5)
            pyautogui.press("enter")
            sleep(0.5)

      elif 'open chrome' in query:
        speak("opening chrome")
        wb.open('Chrome')      
      
      elif 'youtube' in query:
        query = query.replace("friday","")
        query = query.replace("search on" , "")
        query = query.replace("please" , "")
        query = query.replace("youtube" , "")
        search = "https://www.youtube.com/results?search_query="+ query
        wb.open(search)
        pywhatkit.playonyt(query)
        speak("showing reasult on youtube")

      elif 'play' in query:
        query = query.replace("friday","")
        query = query.replace("search on" , "")
        query = query.replace("please" , "")
        query = query.replace("play" , "")
        search = "https://www.youtube.com/results?search_query="+ query
        wb.open(search)
        pywhatkit.playonyt(query)
        speak("showing reasult on youtube")

      elif "remember that" in query:
            query = query.replace("remember that","")
            query = query.replace("friday","")
            query = query.replace("remember","")
            speak("You told me to remember that"+query)
            remember = open("Remember.txt","a")
            remember.write(query)
            remember.close()

      elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me to remember that" + remember.read())
            remember = open("Remember.txt",'w')
            remember.write(f"")
            remember.close()

      elif "schedule my day" in query or 'set today plan' in query:
        tasks = [] #Empty list 
        speak("Do you want to clear old tasks if you want say yes or if you want to add more task to old schedule say no")
        query = connect().lower()
        if "yes" in query:
          file = open("tasks.txt","w")
          file.write(f"")
          file.close()
          speak("how many task do you want plz tell me")
          no_tasks = connect().lower() 
          no_tasks = no_tasks.replace("friday","")
          no_tasks = int(no_tasks)
          i = 0
          speak("now tell me your tasks plz")
          for i in range(no_tasks):
            task = connect().lower()
            tasks.append(task)
            file = open("tasks.txt","a")
            file.write(f"{i}. {tasks[i]}\n")
            file.close()
            speak("next task plz")
          speak("done")  
        elif "no" in query:
          i = 0
          speak("how may task you want to add in your old schedule")
          no_tasks = int(connect().lower())
          no_tasks = no_tasks.replace("friday","")
          speak("now tell me your tasks plz")
          for i in range(no_tasks):
            task = connect().lower()
            tasks.append(task)
            file = open("tasks.txt","a")
            file.write(f"{i}. {tasks[i]}\n")
            file.close()
            speak("next task plz")
          speak("done")  

      elif 'show schedule' in query or 'show today plan' in query:
          file = open("tasks.txt","r")
          content = file.read()
          file.close()
          mixer.init()
          mixer.music.load("notification.mp3")
          mixer.music.play()
          notification.notify(
              title = "My schedule :-",
              message = content,
              timeout = 15
              )
          
      elif 'temperature' in query:
         query = query.replace("friday ","")
         query = query.replace("current ","")
         query = query.replace("now ","")
         query = query.replace("what is the ","")
         url = f"https://www.google.com/search?q={query}"
         result = requests.get(url)
         data = BeautifulSoup(result.text,"html.parser")
         t = data.find("div",class_ = "BNeawe").text
         speak(f"current{query} is {t}")

      elif 'time' in query:
         time = datetime.datetime.now().strftime("%H:%M")
         speak(f" the current time is {time}")   

      elif 'date' in query:
         date  = datetime.datetime.today().strftime("%D")
         day  = datetime.datetime.today().strftime("%A")
         speak(f"today date is {date} and day is {day}")

      elif '.com' in query or '.in' in query or '.co.in' in query or '.org' in query:
         query = query.replace("friday","")
         query = query.replace("open","")
         query = query.replace("website","")
         wb.open(query)

      elif 'generate image ' in query or 'create image' in query or ' create an image' in query or 'create a image' in query or 'generate a image ' in query or 'generate an image' in query:
         query = query.replace('friday','')
         query = query.replace('generate image','')
         query = query.replace('create image','')
         pipe = image_generator.load_model()
         prompt = query
         generated_image_file = image_generator.generate_image(pipe, prompt, output_file=f"generated_image\{random.randrange(0,99999999)}.png")
         image_generator.resize_image(generated_image_file, f"generated_image\{random.randrange(0,99999999)}.png", new_width=3840, new_height=2160)
         img_number = random.randrange(0,99999999)
         image_generator.upscale_image_opencv(generated_image_file,f"generated_image\{img_number}.png", scale=4)
         sleep(1)
         pyautogui.press("super")
         sleep(0.5)
         pyautogui.typewrite(f"{img_number}.png")
         sleep(0.5)
         pyautogui.press("enter")
         speak("opening generated image") 


      elif 'close tab' in query:
         pyautogui.hotkey("crtl","w")

      elif 'close all tabs' in query or  'close all tabs' in query:
         pyautogui.hotkey("Alt","F4")

      elif 'screenshot' in query:
         speak("taking screenshot")
         s = pyautogui.screenshot()
         s.save(f"{random.randint(1,999999999999999999)}.jpg")

      elif 'calculate' in query:
         query = query.replace("friday","")
         query = query.replace("calculate","")
         calu(query)   

      elif 'health problem' in query:
         healthadviser.health_adviser()

      elif 'open' in query:
        query = query.replace("open","")
        query = query.replace("friday","")
        query = query.replace("please","")
        pyautogui.press("super")
        sleep(0.5)
        pyautogui.typewrite(query)
        sleep(0.5)
        pyautogui.press("enter")
        speak("opening" + query ) 

      elif "news" in query:
          from NewsRead import latestnews
          latestnews()        
              
      elif 'friday' in query:
        query = query.replace("friday","")    
        message = query
        ints = predict_class(message)
        res = get_response(ints, intents)
        speak(res)      

      else:
        pass
  else:
    pass    