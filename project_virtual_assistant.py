import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os




engine= pyttsx3.init('sapi5')
rate= engine.getProperty('rate')
# print(rate)
engine.setProperty('rate',145)
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wish():
     hour= int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good morning!")
     elif hour>=12 and hour<18:
          speak("Good Afternoon!")
     else:
          speak("Good evening!!")

     speak("Hello I am Mia. how may i help you.")


def command():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 2
          audio= r.listen(source)
          r.energy_threshold= 400

     try:
          print("Recognizing...")
          query= r.recognize_google(audio, language='en=in')
          print(f"User said:{query}\n")

     except Exception as e:
          # print(e)
          print("say that again please")
          return "None"
     return query


if __name__ == "__main__":
     wish()
     while True:
          query=command().lower()

          #logic excuting tasks based on query
          if 'wikipedia' in query:
               speak('searching wikipedia...')
               query= query.replace("wikipedia","")
               results= wikipedia.summary(query,sentences=2)
               speak("According to wikipedia")
               print(results)
               speak(results)

          elif 'open youtube' in query:
               webbrowser.open("youtube.com")

          elif 'open google' in query:
               webbrowser.open("google.com")

          elif 'open geeksforgeeks' in query:
               webbrowser.open("geeksforgeeks.com")

          # elif 'play music' or query:
               # speak("No song available in your directory")

          elif  'the time' in query:
               strtime=datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"the time is {strtime}")

          elif 'open code' in query:
               codePath="C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
               os.startfile(codePath)
