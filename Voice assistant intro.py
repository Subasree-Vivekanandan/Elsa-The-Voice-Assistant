import warnings
import pyttsx3
import speech_recognition as sr
import pyaudio
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
warnings.filterwarnings("ignore")
obj = pyttsx3.init()
voices = obj.getProperty('voices')        #getting details of current voice
#obj.setProperty('voice', voices[0].id)   #changing index, changes voices. o for male
obj.setProperty('voice', voices[1].id)    #changing index, changes voices. 1 for female

def talk(audio):
    obj.say(audio)
    obj.runAndWait()

def rec_audio():
    recog =sr.Recognizer()
    with sr.Microphone() as source:
          print("Listening.....")
          audio = recog.listen(source)
    data = " "
    try:
        data = recog.recognize_google(audio)
        print("You said: "+data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition"+ex)
    return data

def response(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)

def call(text):
    action_call = "elsa"   # WAKE WORD
    text = text.lower()
    if action_call in text :
        return True
    return False

def say_hello(text):
    greet =["hi","hai","hey","greetings","what's up","hello","howdy","what's good","hey there"]
    response = ["hi","hai","hey","greetings","what's up","hello","howdy","what's good","hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response)+"."
    return ""

def today_date():
    now = datetime.datetime.now()
    date_now= datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]
    return f'Today is {week_now},{months[month_now-1]} the {ordinals[day_now-1]}.'

while True :
    try:
        text = rec_audio()
        speak = " "
        if call (text):          # recognise the WAKE WORD
            speak = speak + say_hello(text)   # greetings
            if "date" in text or "day" in text or "month" in text:   # date,time,day
                get_today = today_date()
                speak=speak+" "+get_today
            elif "time" in text:
                now  = datetime.datetime.now()
                meridiem =""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour -12
                else:
                    meridiem = "a.m"
                    hour = now.hour
                if now.minute < 10:
                   minute = "0"+ str(now.minute)
                else:
                    minute = str(now.minute)

                speak = speak+" "+"It is "+str(hour)+":"+minute+" "+meridiem+" ."


                 #General questions
            elif "who are you" in text or "define yourself" in text:
                speak =speak+"""Hello ,Elsa is my name , Helping you is my game. I am here to make your life easier. You can command me to perform various tasks"""
            elif "your name" in text:
                speak = speak + " My name is elsa"
            elif "who am i" in text:
                speak = speak + "You must probably be a human"
            elif "how are you" in text:
                speak = speak + "I am fine,Thank you for asking.This is a challenging time for us.I hope you and your loved ones are staying safe and healthy."
                speak =speak+"\nHow are you?"
            elif "i am fine" in text or "i am good" in text:
                speak =speak + "I am glad to know that you are fine"

            response(speak)
    except:
        talk("I don't know that")

