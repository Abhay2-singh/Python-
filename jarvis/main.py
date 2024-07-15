import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
 
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d4c1b583146a481c95dbd1120f78e598"
# pip install pocketsphinx

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
     tts = gTTS(text)
     tts.save('temp.mp3')
         # Initialize Pygame mixer
     pygame.mixer.init()

    # Load the MP3 file
     pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
     pygame.mixer.music.play()

    # Keep the program running until the music stops playing
     while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
     pygame.mixer.music.unload()
     os.remove("temp.mp3") 
     


 
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif"open facebook " in c.lower():
        webbrowser.open("http://facebook.com")
    elif"open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif"open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif"open instagrame" in c.lower():
        webbrowser.open("http://instagrame.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.getget(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
               speak(article['title'])
    else:
        #let open ai handle the request
        pass


   
if __name__== "__main__":
    speak("Initializing jarvis....")
    while True:
        #listen for the wake word "jarvis"
        #obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using google
        print("recognizing...")
        try:
           with sr.Microphone() as source:
             print("Listening...")
             audio = r.listen(source,timeout=2,phrase_time_limit=1)
           word = r.recognize_google(audio)
           if(word.lower()=="jarvis"):
                speak("yes")
                #listen for command
                with sr.Microphone() as source:
                     print("jarvis active....")
                     audio = r.listen(source)
                     command = r.recognizer_google(audio)
                     processcommand(command)
   
        except Exception as e:
            print("error; {0}".format(e))

