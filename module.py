import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import random
import os
import psutil
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # You can change the voice index for different voices

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listens for voice input and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def greet():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your personal assistant. How can I help you?")

def tell_joke():
    """Tells a random joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? He was outstanding in his field!",
        "Why don't eggs tell jokes? They'd crack each other up!",
        "What do you call a fake noodle? An impasta!"
    ]
    joke = random.choice(jokes)
    speak(joke)

def do_calculation(command):
    """Performs basic calculations."""
    try:
        expression = command.replace("calculate", "").replace("math", "").strip()
        result = eval(expression)
        speak(f"The result is {result}")
    except:
        speak("Sorry, I couldn't perform that calculation.")

def system_info():
    """Provides system information."""
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    speak(f"CPU usage is {cpu_percent} percent. Memory usage is {memory.percent} percent.")

def web_search(command):
    """Performs web search."""
    query = command.replace("search", "").strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching for {query}")

def search_wikipedia(command):
    """Searches Wikipedia."""
    query = command.replace("wikipedia", "").strip()
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        speak("Sorry, I couldn't find information on Wikipedia.")

if __name__ == "__main__":
    greet()
    while True:
        command = take_command().lower()

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "open youtube" in command:
            webbrowser.open("youtube.com")
            speak("Opening YouTube.")

        elif "joke" in command:
            tell_joke()

        elif "calculate" in command or "math" in command:
            do_calculation(command)

        elif "system info" in command:
            system_info()

        elif "search" in command:
            web_search(command)

        elif "wikipedia" in command:
            search_wikipedia(command)

        elif "open notepad" in command:
            os.system("notepad")
            speak("Opening Notepad.")

        elif "shutdown" in command:
            speak("Shutting down the system.")
            os.system("shutdown /s /t 1")

        elif "restart" in command:
            speak("Restarting the system.")
            os.system("shutdown /r /t 1")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
