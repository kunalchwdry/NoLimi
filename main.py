from system.process import process
from speaker.speaker import speak
from AI.AI import aiprocess
import speech_recognition as sr
rec = sr.Recognizer()        
if __name__ == "__main__":
    speak("Initializing Nolimiiii....")
    while True:
        with sr.Microphone() as source:
            print("to talk speak nolimi...")
            
            try:
                audio = rec.listen(source, timeout=5, phrase_time_limit=5)
                rec.adjust_for_ambient_noise(source, duration=1)
                command = rec.recognize_google(audio)
                command = command.lower().strip()

                print(repr(command))

                if command in [
                    "Nolimi",
                    "hello",
                    "hi",
                    "oye",
                    "oye sun",
                    "oye Nolimi",
                    "oye hello",
                    "oye bro",
                    "oye buddy",
                    "oye friend",
                    "oye mate"
                ]:
                    speak(" how can i help u")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        try:
                            audio = rec.listen(source, timeout=5, phrase_time_limit=5)
                        except sr.WaitTimeoutError:
                            print("No speech detected.")
                            continue
                    command = rec.recognize_google(audio).lower().strip()
                    print(command)
                    process(command)
                elif "exit" in command:
                    speak("Exiting nolimi byeee!")
                    exit()

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand.")

            except sr.RequestError as e:
                print("Google Speech Recognition error:", e)
                
            
           
    