import os
from dotenv import load_dotenv
from google import genai
from speaker import speak

# Load variables from .env
load_dotenv()

# Read API key
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def aiprocess(c):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "You are NoLimi, an AI-powered virtual assistant skilled in various general tasks. Give concise answers in 2-3 sentences.",
            c
        ]
    )

    print(response.text)
    speak(response.text)