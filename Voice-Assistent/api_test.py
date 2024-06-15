import requests
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyA7rTu6wr54MncVzu-rvANFcklBXMPo-mw")
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)





# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set properties for the TTS engine
tts_engine.setProperty('rate', 150)  # Speed of speech
tts_engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

def speak(text):
     tts_engine.say(text)
     print(text)
     tts_engine.runAndWait()

   

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_date():
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

def ask_gemini(question):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(question)
    return response.text

def get_weather(city):
    api_key = "2696fc62b67540cd9bf6646287b8e0992"
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    weather_data = response.json()
    
    if weather_data["cod"] == 200:
        main = weather_data["main"]
        weather = weather_data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        return f"The weather in {city} is {description} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't fetch the weather for that location."



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
    elif "what is" in command or "who is" in command or "tell me about" in command:
        answer = ask_gemini(command)
        speak(answer)
    elif "weather" in command:
        city = command.replace("weather in", "").strip()
        response = get_weather(city)
        speak(response)
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
