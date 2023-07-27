import pyttsx3 #import pyttsx3 model
import datetime as dt # Import date and time
import speech_recognition as sr # Import speech recognition
import wikipedia # import wikipedia
import smtpd # Import library to send emails
import webbrowser as wb # Import the webbrowser library to help the program access the web browser
import os # Import the operating system library
import pyautogui # import the pyautogui library
import psutil # import the ps util library
import pyjokes #import pyjokes

engine = pyttsx3.init() #Created and initialised an object for the ai package

voices = engine.getProperty('voices') #This code changes the voice
engine.setProperty('voice', voices[0].id)
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
    speak("How can i help you today?")

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

def  sendmail(to, content):
    speak("Please enter your email: ")
    email = input("Please enter your email: ")
    speak("Please enter your password: ")
    pword = input("Please type your password")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, pword )
    server.sendmail(email, to, content)
    server.close()

# def screenshot():
#     img = pyautogui.screenshot()
#     img.save("C:\Users\raymo\ai_assistant\ss.jpg")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery
    speak("battery is at" + battery.percent)

def jokes():
    speak(pyjokes.get_joke())


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
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 3)
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                speak("Please provide receipients email: ")
                to = input("Please provide receipients email: ")
                sendmail(to, content)
                speak(content)
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "chrome" in query:
            speak("What should I search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        # elif "play songs" in query:
        #     song_dir = "C:\Users\raymo\Music\iTunes\iTunes Media\Apple Music"
        #     songs = os.listdir(song_dir)
        #     os.startfile(os.path.join(song_dir, songs[0]))
        elif "remember" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You told me to remember that" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Screenshot done!")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
