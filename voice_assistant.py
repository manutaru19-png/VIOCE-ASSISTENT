import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Could not understand")
        return ""

speak("Voice assistant started")

while True:
    command = listen()

    # GOOGLE
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # YOUTUBE
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # WHATSAPP WEB
    elif "whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open_new_tab("https://web.whatsapp.com")

    # INSTAGRAM
    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open_new_tab("https://www.instagram.com")

    # OPEN CHROME
    elif "chrome" in command:
        speak("Opening Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    # OPEN VS CODE
    elif "vscode" in command or "visual studio code" in command:
        speak("Opening Visual Studio Code")
        os.startfile("C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    # TIME
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    # SHUTDOWN
    elif "shutdown" in command:
        speak("Shutting down computer")
        os.system("shutdown /s /t 5")

    # EXIT
    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break