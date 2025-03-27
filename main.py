import speech_recognition as sr
import webbrowser
import pyttsx3
import songs
from gtts import gTTS
import pygame 
import os

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open('https://google.com')
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = songs.musics.get(song)
        if link:
            webbrowser.open(link)
        else:
            print("Song not found.")
    print(c)

if __name__ == "__main__":
    speak("jarvis is running....")

    while True:
        try:
            with sr.Microphone() as source:
              
                r.adjust_for_ambient_noise(source)
                print("Say something...")
               
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                print("Recognizing...")

            word = r.recognize_google(audio)
            if word.lower() == 'jarvis':
                speak('yes bro!')
                with sr.Microphone() as source:
                    print("Listening for command...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)   
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print(f"Recognition error: {e}")
