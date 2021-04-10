# importing the pyttsx library 
import pyttsx3 
import datetime
import wikipedia
import  webbrowser
import os
from googlesearch import search
import speech_recognition as sr

r = sr.Recognizer()  

def speak(msg):
    # initialisation 
    engine = pyttsx3.init() 
    engine.say(msg)
    engine.runAndWait() 

def wish():
    h = datetime.datetime.now().hour
    if(h<12 and h>4):
        speak("good morning")
    elif(h>=12 and h<17):
        speak("good afternoon")
    elif(h>=17 and h<19) :
        speak("good evening")
    else:
        speak("good night")  

def takecommand():
    while(1):
        try:
            with sr.Microphone() as source2: 
                r.adjust_for_ambient_noise(source2, duration=0.2) 
                audio2 = r.listen(source2) 
                MyText = r.recognize_google(audio2) 
                #MyText = MyText.lower() 
                print("you said "+MyText) 
                return MyText 
        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
            speak("Try again")
            
        except sr.UnknownValueError: 
            print("unknown error occured") 
            speak("Try again")
      
if __name__== "__main__":
    wish()
    speak("hello Rashmi i am Alexa. what i can do for you")
    #takecommand()
    while True :
        speak("Please tell")
        #q = input("yes tell:") 
        q = takecommand()
        if('search' in q or 'tell' in q):
            print("Searching at wikipedia ...")
            a = q.replace('search', ' ')
            result = wikipedia.summary(a, sentences = 5)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif('thank you' in q):
            speak("Alexa's Pleasure !!")
        elif('date' in q):
            now =  datetime.datetime.now()
            speak(f'according to india date is ')
            speak(now.strftime('on %A, %d date %B month, %Y'))
            print(now.strftime('on %A, %d date %B month, %Y'))
        elif('done' in q):
            speak("Bye Rashmi, meet you next time")
            break
        elif('open Google' in q):
            webbrowser.open("google.com")
            t = input()
            if(t=='e'):
                break
        elif('open YouTube' in q):
            webbrowser.open("youtube.com")
            t = input()
            if(t=='e'):
                break
        elif('time' in q):
            speak(f'As per indian standar time is {datetime.datetime.now().hour}hours {datetime.datetime.now().minute} minutes {datetime.datetime.now().second} seconds')
            print(f'{datetime.datetime.now().hour} hours {datetime.datetime.now().minute} minutes {datetime.datetime.now().second} seconds')
        elif(q):
            for j in search(q, tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
                webbrowser.open(f'{j}')
            t = input()
            if(t=='e'):
                break
        else:
            speak("say again")