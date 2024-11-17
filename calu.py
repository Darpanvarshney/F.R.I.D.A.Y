import wolframalpha
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voicespeed = 150
engine.setProperty('rate', voicespeed)

 #audio pass
def speak(audio) :
  engine.say(audio)
  engine.runAndWait()

def wolf(query):
    apikey = "enter for api key"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        ans= next(requested.results).text
        return ans
    except:
        speak("answer is not answerable")

def calu(query):
    term = str(query)
    term = term.replace("friday","")
    term = term.replace("calculate","")
    term = term.replace("add","+")
    term = term.replace("pluse","+")
    term = term.replace("minus","-")
    term = term.replace("multiply","*")
    term = term.replace("into","*")
    term = term.replace("divide","/")
    term = term.replace("power","**")

    try:
        result = wolf(term)
        print(result)
        speak(result)
    except:
        speak("sorry the value is not answerable")    
    
