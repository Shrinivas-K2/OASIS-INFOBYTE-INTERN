import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set properties for the TTS engine
tts_engine.setProperty('rate', 150)  # Speed of speech
tts_engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, the service is down.")
            return ""

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        current_time = get_time()
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = get_date()
        speak(f"Today's date is {current_date}")
    elif "search for" in command:
        search_query = command.replace("search for", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {search_query}")
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Voice assistant is now active.")
    while True:
        command = listen()
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        handle_command(command)
