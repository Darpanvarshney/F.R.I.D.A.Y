import pyttsx3
import speech_recognition as sr
from googletrans import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voicespeed = 150
engine.setProperty('rate', voicespeed)

 #audio pass
def speak(audio) :
  engine.say(audio)
  engine.runAndWait()

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

def health_adviser():
    speak("Welcome to the Health Adviser!")
    speak("Please describe your symptoms (speak 'done' when finished):")
    symptom = connect().lower()
    symptom = symptom.replace("i have","")
    symptom = symptom.replace("friday","")
    symptom = symptom.replace("and","")
    symptom = symptom.replace("some","")
    symptom = symptom.replace("i had","")
    symptom = symptom.split()
    print(symptom)
  
    if not symptom:
        speak("No symptoms provided. Exiting.")
        return

    speak("\nBased on your symptoms, here are some general recommendations:")
    for symptom in symptom:
        if symptom == 'fever':
            speak("- Rest and stay hydrated.")
            speak("- Take over-the-counter fever reducers like acetaminophen or ibuprofen if necessary.")
        elif symptom == 'cough' or symptom == 'sore throat':
            speak("- Drink warm liquids.")
            speak("- Use throat lozenges or cough drops.")
            speak("- Consider over-the-counter cough suppressants or expectorants.")
        elif symptom == 'headache':
            speak("- Get plenty of rest.")
            speak("- Apply a cold pack to your forehead or neck.")
            speak("- Consider over-the-counter pain relievers like acetaminophen or ibuprofen.")
        elif symptom == 'fatigue' or symptom == 'tiredness':
            speak("- Ensure you are getting enough sleep.")
            speak("- Eat a balanced diet and stay hydrated.")
            speak("- Consider reducing stress and practicing relaxation techniques.")
        elif symptom == 'nausea' or symptom == 'vomiting':
            speak("- Stay hydrated by sipping clear fluids.")
            speak("- Eat bland foods like crackers or toast.")
            speak("- Avoid spicy, fatty, or overly sweet foods.")
        elif symptom == 'diarrhea':
            speak("- Stay hydrated by drinking clear fluids like water, broth, or oral rehydration solutions.")
            speak("- Eat bland, low-fiber foods like rice, bananas, or boiled potatoes.")
            speak("- Avoid dairy products, caffeine, and high-fat foods until symptoms improve.")
        elif symptom == 'chest pain' or symptom == 'shortness of breath':
            speak("- Seek emergency medical attention immediately.")
            speak("- Do not wait, call emergency services.")
        elif symptom == 'abdominal pain' or symptom == 'stomach ache':
            speak("- Rest and apply a warm compress to the abdomen if the pain is mild.")
            speak("- Avoid solid foods until the pain subsides.")
            speak("- If the pain is severe or persistent, seek medical attention.")
        elif symptom == 'muscle aches' or symptom == 'joint pain':
            speak("- Rest and apply ice packs to the affected area.")
            speak("- Take over-the-counter pain relievers like ibuprofen or naproxen if necessary.")
            speak("- Stretch gently and avoid strenuous activities until the pain improves.")
        elif symptom == 'rash' or symptom == 'skin irritation':
            speak("- Keep the affected area clean and dry.")
            speak("- Avoid scratching or picking at the rash.")
            speak("- Apply soothing lotions or creams, such as calamine or hydrocortisone.")
        elif symptom == 'dizziness' or symptom == 'lightheadedness':
            speak("- Sit or lie down in a safe place to prevent falls.")
            speak("- Drink water or a sports drink to stay hydrated.")
            speak("- If symptoms persist or worsen, seek medical attention.")
        elif symptom == 'backpain':
            speak("- Apply heat or cold packs to the affected area.")
            speak("- Practice gentle stretching exercises.")
            speak("- Consider over-the-counter pain relievers like ibuprofen or acetaminophen.")
        elif symptom == 'difficulty breathing' or symptom == 'wheezing':
            speak("- Sit upright and try to relax.")
            speak("- Use a rescue inhaler if you have one.")
            speak("- Seek medical help immediately if symptoms are severe or worsen.")
        elif symptom == 'urinary urgency' or symptom == 'frequent urination':
            speak("- Drink plenty of water to stay hydrated.")
            speak("- Avoid caffeine and alcohol, which can irritate the bladder.")
            speak("- Consult a doctor if symptoms persist or are accompanied by pain or discomfort.")
        elif symptom == 'blood in stool' or symptom == 'rectal bleeding':
            speak("- Seek medical attention immediately.")
            speak("- Avoid aspirin and nonsteroidal anti-inflammatory drugs (NSAIDs) until evaluated by a doctor.")
            speak("- Do not ignore this symptom as it could indicate a serious condition.")
        elif symptom == 'vision changes' or symptom == 'blurred vision':
            speak("- Rest your eyes and avoid straining them.")
            speak("- If wearing glasses or contact lenses, ensure they are clean and properly adjusted.")
            speak("- Consult an eye doctor if symptoms persist or worsen.")
        elif symptom == 'unexplained weight loss':
            speak("- Keep track of your diet and eating habits.")
            speak("- Consult a doctor to rule out any underlying medical conditions.")
            speak("- Monitor for other symptoms such as fatigue or changes in appetite.")
        elif symptom == 'swollen glands' or symptom == 'lymph nodes':
            speak("- Apply a warm compress to the affected area.")
            speak("- Get plenty of rest and stay hydrated.")
            speak("- Consult a doctor if swelling persists or is accompanied by other symptoms.")
        elif symptom == 'acid reflux' or symptom == 'heartburn':
           speak("- Avoid spicy, acidic, or fatty foods that can trigger symptoms.")
           speak("- Eat smaller meals and avoid lying down after eating.")
           speak("- Consider over-the-counter antacids or acid reducers.")
        elif symptom == 'constipation' or symptom == 'difficulty passing stool':
           speak("- Drink plenty of water and eat high-fiber foods like fruits, vegetables, and whole grains.")
           speak("- Exercise regularly to promote bowel movements.")
           speak("- Consider over-the-counter laxatives if symptoms persist.")
        elif symptom == 'anxiety' or symptom == 'panic attacks':
           speak("- Practice deep breathing exercises or meditation to reduce stress.")
           speak("- Engage in regular physical activity to help manage anxiety.")
           speak("- Consider therapy or counseling for additional support.")
        elif symptom == 'depression' or symptom == 'low mood':
           speak("- Reach out to friends, family, or a mental health professional for support.")
           speak("- Engage in activities you enjoy and set small, achievable goals.")
           speak("- Consider therapy, medication, or other treatments as recommended by a healthcare provider.")
        elif symptom == 'insomnia' or symptom == 'difficulty sleeping':
           speak("- Establish a regular sleep schedule and create a relaxing bedtime routine.")
           speak("- Avoid caffeine, alcohol, and electronic devices before bed.")
           speak("- Consider relaxation techniques or over-the-counter sleep aids if necessary.")
        elif symptom == 'earache' or symptom == 'ear pain':
           speak("- Apply a warm compress to the affected ear to relieve pain.")
           speak("- Avoid inserting objects into the ear canal, including cotton swabs.")
           speak("- Consider over-the-counter pain relievers like ibuprofen or acetaminophen.")
        elif symptom == 'toothache' or symptom == 'dental pain':
           speak("- Rinse your mouth with warm salt water to reduce swelling and discomfort.")
           speak("- Avoid chewing on the side of the mouth with the affected tooth.")
           speak("- Consider over-the-counter pain relievers like ibuprofen or acetaminophen.")
        elif symptom == 'hay fever' or symptom == 'allergies':
           speak("- Avoid exposure to known allergens, such as pollen, dust, or pet dander.")
           speak("- Use over-the-counter or prescription antihistamines as recommended by a doctor.")
           speak("- Consider allergy shots or immunotherapy for long-term management of symptoms.")
        elif symptom == 'sprain' or symptom == 'strain':
           speak("- Rest the affected area and avoid putting weight on it if possible.")
           speak("- Apply ice packs to reduce swelling and pain.")
           speak("- Elevate the injured limb and consider using a compression bandage.")
        elif symptom == 'sunburn' or symptom == 'sun exposure':
           speak("- Apply cool compresses or take cool baths to soothe the skin.")
           speak("- Use moisturizers or aloe vera gel to hydrate and soothe sunburned skin.")
           speak("- Drink plenty of water to stay hydrated and promote healing.")
        elif symptom == 'poison ivy' or symptom == 'contact dermatitis':
           speak("- Wash the affected area with soap and water to remove any plant oils.")
           speak("- Apply calamine lotion or hydrocortisone cream to reduce itching and inflammation.")
           speak("- Avoid scratching or rubbing the rash, as this can cause further irritation.")
        elif symptom == 'sprain' or symptom == 'strain':
           speak("- Rest the affected area and avoid putting weight on it if possible.")
           speak("- Apply ice packs to reduce swelling and pain.")
           speak("- Elevate the injured limb and consider using a compression bandage.")  
        else:
            speak(f"- Sorry, I'm not familiar with advice for '{symptom}'. Please consult a healthcare professional.")

    speak("\nPlease consult a healthcare professional if your symptoms persist or worsen.")
