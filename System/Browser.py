import webbrowser
import ddgs
from speaker.speaker import speak

def webopen(c):
        try:
            query = c[5:].strip()  # Removes "open "
            results = ddgs.DDGS().text(query, max_results=5)
            blocked = ["wiki", "pedia", "media", "encyclo"]
            for i in results:
                if any(word in i["href"].lower() for word in blocked):
                    continue
            
                speak(f"Opening {query}")
                webbrowser.open(i['href'])
                break
            else:
                speak(f"Sorry, I couldn't find any results for {query}.")
        except Exception as e:
            print(f"Error occurred :{e}")
            speak(f"Sorry, I encountered an error while searching the site.") 