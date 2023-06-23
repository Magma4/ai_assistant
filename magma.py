import pyttsx3 #import pyttsx3 model
import datetime as dt

engine = pyttsx3.init() #Created and initialised an object for the ai package

voices = engine.getProperty('voices') #This code changes the voice
engine.setProperty('voice', voices[1].id)
newVoiceRate = 160
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("Hello, I am your AI assistant. You can ask me anything.")

def time():
    Time = dt.datetime.now().strftime("%I:%M:%S")
    speak("The time is " + Time)

# time()

def date():
    year = int(dt.datetime.now().year)
    month = str(dt.datetime.now().month)
    day = int(dt.datetime.now().day)
    speak(f"The current date is {day} {month} {year}")

date()
