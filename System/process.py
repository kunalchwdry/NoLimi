import webbrowser
import requests
import requests
from speaker import speak
from AI import aiprocess
from application import application
import pywhatkit
from dotenv import load_dotenv
from googlesearch import search
import os
from pywhatkit import playonyt
load_dotenv()
from Browser import webopen
import re
from volume import handle_volume
from Brightness import handle_brightness
newsapi = os.getenv("NEWS_API_KEY")
def process(c):
    if application(c):
        return
        
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c.lower():#edit
        webbrowser.open("https://spotify.com")

    elif "open github" in c.lower():#edit
        webbrowser.open("https://github.com")

    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")

    elif "open gemenai" in c.lower():#edit
        webbrowser.open("https://gemini.com")
    elif any(x in c.lower() for x in [
    "volume",
    "mute",
    "increase volume",
    "decrease volume",
    "getvolume"
    ]):
        handle_volume(c, speak)
    elif any(word in c.lower() for word in [
    "brightness",
    "increase brightness",
    "decrease brightness",
    "set brightness",
    "maximum brightness",
    "minimum brightness",
    "current brightness",
    "get brightness"
    ]):
        handle_brightness(c)
    elif c.lower().startswith("open"):
        webopen(c)
    elif c.lower().startswith("play"):
        query = c[5:]  # Removes "play "
        speak(f"Playing {query}")
        pywhatkit.playonyt(query)
    elif "time" in c.lower():
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "news" in c.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            articles = data["articles"]
            speak("Here are the top headlines.")
            for article in articles[:5]:
                print(article["title"])
                speak(article["title"])
        else:
             speak("Sorry, I couldn't fetch the news.")
    elif "exit" in c.lower(): # pyright: ignore[reportUnknownMemberType]
        speak("Exiting nolimi byeee!")
        exit()
    else:
        #let genai handel the acc
        aiprocess(c)