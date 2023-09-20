import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os.path

engine = pyttsx3.init('sapi5') #initialie the pyttsx3 with the sapi5
voices = engine.getProperty('voices') #gets you the details of the current voice
engine.setProperty('voice', voices[0].id) #0 for male, 1 for female

def say(audio): #speak function that makes assistant talk hihi
    engine.say(audio)
    engine.runAndWait() #part of the pyttsx3 lib, without this, speech wont be audible 

def greetings():
    hour = int(datetime.datetime.now().hour) #datetime.datetime shows time form the year to the microsecond 
    if 0<=hour<12:
        say("Good morning")

    elif 12<hour<18:
        say("Good afternoon")

    else:
        say("Good evening")

    say("How can I help you?")

def AudioInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:  
        print("Listening")
        r.pause_threshold = 2 
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language = "en-US")
        print(f'User said: {query}\n')   #the 'f' is used to print the {query} depending on what it can be 
        say(f'User said: {query}\n')
        
    except Exception as e: 
        say("Could you repeat that?")
        return 'None'
    return query

if __name__ in '__main__': 
    greetings()
    while True:
        query = AudioInput().lower() #turns spoken commands to lowercase  
        
        #expand these commands for more possibilities + try to add openai to them somehow 

        if 'google' in query:
            say('opening google')
            webbrowser.open('google.com')

        elif 'youtube' in query:
            say('opening youtube')
            webbrowser.open('youtube.com')


        elif 'github' in query: 
            say('opening github')
            webbrowser.open('github.com')

        elif 'netflix' or 'movie' in query:
            say('opening netflix')
            webbrowser.open('netflix.com')
            
        elif 'wikipedia' in query: 
            say('searching wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentenecs = 8)
            print(results)
            say(results)
            
        elif 'leave'or 'exit' or 'quit' in query:
            say('good day')
            quit()







