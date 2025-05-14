
import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
import wikipedia
import webbrowser
import joblib

# Load trained intent model
model = joblib.load("intent_model.pkl")

# Voice assistant setup
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[14].id)  # Adjust if needed
engine.setProperty('rate', 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Network error.")
        return ""

def process_command(command):
    if not command:
        return
    intent = model.predict([command])[0]

    if intent == "greet":
        speak("Hello! How can I assist you?")
    elif intent == "time":
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {current_time}")
    elif intent == "joke":
        speak(pyjokes.get_joke())
    elif intent == "wikipedia":
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia:")
            speak(summary)
        except:
            speak("Couldn't find anything.")
    elif intent == "open_site":
        if "youtube" in command:
            webbrowser.open("https://www.youtube.com")
        elif "google" in command:
            webbrowser.open("https://www.google.com")
        else:
            site = command.split()[-1]
            webbrowser.open(f"https://{site}.com")
    elif intent == "exit":
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure what you meant.")

# Main loop
if __name__ == "__main__":
    speak("Hi! I am your AI assistant. How can I help you?")
    while True:
        command = listen()
        process_command(command)
