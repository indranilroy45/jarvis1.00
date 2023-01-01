import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
#print (voices[1] .id)
engine.setProperty('voice', voices[1].id)

def speak (audio):
    pass
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour< 12:
        speak("Good morning!")

    elif hour>=12 and hour< 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am jarvice, pleas tell me, how can I help You")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
            print(f"User said: {query}\n")  # User query will be printed.

        except Exception as e:
            # print(e)
            print("Say that again please...")  # Say that again will be printed in case of improper voice
            return "None"  # None string will be returned
        return query

if __name__ == "__main__":
    pass
wishme()
query = takeCommand().lower()  # Converting user query into lower case

# Logic for executing tasks based on query
if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)
elif 'open youtube' in query:
    webbrowser.open("youtube.com")

elif 'open facebook' in query:
    webbrowser.open("facebook.com")

if 'play' in query:
    speak('playing from Youtube... ')
    query = query.replace('play', '')
    results = pywhatkit.playonyt(query)

elif 'who are you' in query:
    speak('I am Jarvis 1.00,  maid by Indranil Roy in fast january 2023')

