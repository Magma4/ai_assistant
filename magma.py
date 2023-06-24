import pyttsx3 #import pyttsx3 model
import datetime as dt # Import date and time
import speech_recognition as sr # Import speech recognition

engine = pyttsx3.init() #Created and initialised an object for the ai package

voices = engine.getProperty('voices') #This code changes the voice
engine.setProperty('voice', voices[1].id)
newVoiceRate = 160
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    """This is the speak function"""
    engine.say(audio)
    engine.runAndWait()

# speak("Hello, I am your AI assistant. You can ask me anything.")

def time():
    """This function tell the current time"""
    Time = dt.datetime.now().strftime("%I:%M:%S")
    speak("The time is " + Time)

# time()

def date():
    """This function tells the current date"""
    year = int(dt.datetime.now().year)
    month = int(dt.datetime.now().month)
    day = int(dt.datetime.now().day)
    speak(f"The current date is {day} {month} {year}")

# date()

def wishMe():
    """This function let's magma greets the user when started"""
    speak("Welcome back sir!")
    # time()
    # date()
    hour = dt.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Magma at your service, how can i help you today?")

# wishMe()

def takeCommand():
    """Take command from user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Come again please...")

        return "None"
    
    return query

#takeCommand()

if __name__ == "__main__":

    wishMe()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Going off")
            quit()