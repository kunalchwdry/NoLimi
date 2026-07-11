from gtts import gTTS
import pygame
import os
import speech_recognition as sr
import pyttsx3
rec = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text):
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("temp.mp3")
    pygame.mixer.init()

    pygame.mixer.music.load("temp.mp3")  # Path to your MP3
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
def old_speak(text):
    global ttsx
    ttsx.stop()
    ttsx.say(text)
    ttsx.runAndWait()