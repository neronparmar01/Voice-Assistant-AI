import speech_recognition as sr
import pyttsx3
import datetime
import sys
import getpass
import requests
from geopy.geocoders import Nominatim

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the geocoder
geolocator = Nominatim(user_agent="Jarvis")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

#getting the locations
def get_location():
    while True:
        try:
            # Fetch the user's IP address
            ip_info = requests.get('https://api64.ipify.org?format=json').json()
            ip_address = ip_info['ip']
            
            # Reverse geocode the IP address to get the location
            location = geolocator.reverse(ip_address)
            
            return location.address
        except Exception as e:
            print("Error getting location:", e)
            return "unknown location"
        time.sleep(60)  # Update location every minute

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
        
    # name commands 
    elif "What's my name?" in command or "Say my name" in command or "My name" in command or "My name?" in command:
        speak("Your name is Neron Parmar!")
    elif "What's my full name?" in command or "Say my full name" in command or "My full name" in command or "My full name?" in command or "Full name" in command:
        speak("Your name is Neron Nelson Parmar!")
    # ------------------for lower case (name)----------------------    
    elif "what's my name?" in command or "say my name" in command or "my name" in command or "my name?" in command:
        speak("Your name is Neron Parmar!")
    # ------------------for lower case (full name)----------------------
    elif "what's my full name?" in command or "say my full name" in command or "my full name" in command or "my full name?" in command or "full name" in command:
        speak("Your name is Neron Nelson Parmar!")
    
    # time commands
    elif "Time" in command or "Time?" in command or "What's the current Time?" in command or "What's the time?" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak("The current time is " + current_time)
    # ------------------for lower case (time)----------------------    
    elif "what's the current time?" in command or "time" in command or "What's the time?" in command or "time?" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak("The current time is " + current_time)
    
    # date commands
    elif "Date" in command or "Date?" in command or "What's today's date?" in command or "Today's date?" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak("Today's date is " + current_date)
    # ------------------for lower case (date)----------------------
    elif "date" in command or "date?" in command or "what's today's date?" in command or "today's date" in command or "what is today's date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak("The current date is " + current_date)
   
    # day commands   
    elif "Day" in command or "Day?" in command or "What's today's day?" in command or "Today's Day?" in command:
        current_day = datetime.datetime.now().strftime("%B")
        speak("Today's day is " + current_day)
    # ------------------for lower case (Day)----------------------
    elif "day" in command or "day?" in command or "what's today's day?" in command or "today's Day?" in command:
        current_day = datetime.datetime.now().strftime("%B")
        speak("Today's day is " + current_day)
        
    # location commands
    elif "Location" in command or "Location?" in command or "What's my current location?" in command or "What's my location" in command:
        location = get_location()
        speak("You are currently at " + location)
    # ------------------for lower case (location)---------------------- 
    elif "location" in command or "location?" in command or "what's my current location?" in command or "what's my location" in command:
        location = get_location()
        speak("You are currently at " + location)

    # pause commands
    elif "pause" in command or "stop" in command or "wait" in command:
        speak("Pausing Jarvis. Let me know when you need me again.")
        return "pause"
    
    # quit commands
    elif "goodbye" in command or "exit" in command or "quit" in command:
        speak("Ok, Bye!")
        exit()
    else:
        speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis. How can I assist you?")
    paused = False
    while True:
        if not paused:
            command = listen()
            if command == "pause":
                paused = True
            else:
                process_command(command)
        else:
            input("Press Enter to resume Jarvis...")
            speak("Resuming Jarvis.")
            paused = False