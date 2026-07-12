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
import ddgs
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
    elif c.lower().startswith("open"):
        try:
            query = c[5:].strip()  # Removes "open "
            results = ddgs.DDGS().text(query, max_results=5)
            for i in results:
                if "wiki" in i['href']:
                    continue
                elif "encyclo"in i['href']:
                    continue
                elif "media" in i['href']:
                    continue
                elif 'pedia' in i['href']:
                    continue
                else:
                    speak(f"Opening {query[1:]}")
                    webbrowser.open(i['href'])
                    break
            else:
                speak(f"Sorry, I couldn't find any results for {query}.")
        except Exception as e:
            print(f"Error occurred :{e}")
            speak(f"Sorry, I encountered an error while searching the site.") 
    
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