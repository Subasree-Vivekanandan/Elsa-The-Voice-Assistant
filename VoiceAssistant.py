from __future__ import print_function
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
import ctypes
import winshell
import subprocess
import pyjokes
import smtplib
import requests
import json
import time
import os.path
from twilio.rest import Client
import wolframalpha
import pickle
import os.path

from selenium import webdriver
from time import sleep


warnings.filterwarnings("ignore")
obj = pyttsx3.init()
voices = obj.getProperty('voices')       #getting details of current voice
obj.setProperty('voice', voices[0].id)   #changing index, changes voices. o for male
#obj.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female

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
    action_call = "elsa"   #WAKE WORD
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


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0,len(list_wiki)):
        if i+3 <= len(list_wiki)-1 and list_wiki[i].lower()=="who" and list_wiki[i+1].lower() == "is":
            return list_wiki[i+2]+" "+list_wiki[i+3]

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login('subhasrii2019@gmail.com', 'subha@123')
    server.sendmail("subhasrii2019@gmail.com", to,content )
    server.close()

def pizza():
    driver = webdriver.Chrome(r"C:\Users\HP\Desktop\chromedriver.exe")
    driver.maximize_window()

    talk("Opening Dominos")
    driver.get('https://www.dominos.co.in/')
    sleep(2)

    talk("Getting ready to order")
    driver.find_element_by_link_text('ORDER ONLINE NOW').click()
    sleep(2)

    talk("Finding your location")

    driver.find_element_by_class_name('srch-cnt-srch-inpt').click()
    sleep(2)

    location = "psg college of technology"
    talk("Entering your location")
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input').send_keys(location)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div[2]').click()
    sleep(2)

    driver.get('https://pizzaonline.dominos.co.in/menu')


    try:
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[1]').click()
        sleep(2)
    except:
        talk("Your location could not be found. Please try again later.")
        exit()

    talk("Logging in")
    phone_num = "9486973639"

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(
        phone_num)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
    sleep(2)

    talk("What is your O T P? ")
    sleep(3)

    otp_log = rec_audio()

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(otp_log)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()
    sleep(2)

    talk("Do you want me to order from your favorites?")
    query_fav = rec_audio()

    if "yes" in query_fav:
        try:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[6]/div/div/div[2]/div[3]/div/button/span').click()
            sleep(1)
        except:
            talk("The entered OTP is incorrect.")
            exit()

        talk("Adding your favorites to cart")

        talk("Do you want me to add extra cheese to your pizza?")
        ex_cheese = rec_audio()
        if "yes" in ex_cheese:
            talk("Extra cheese added")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[2]/button').click()
        elif "no" in ex_cheese:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
        else:
            talk("I dont know that")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()

        driver.find_element_by_xpath(
            '//*[@id="mn-lft"]/div[16]/div/div[1]/div/div/div[2]/div[2]/div/button').click()
        sleep(1)

        talk("Would you like to increase the qty?")
        qty = rec_audio()
        qty_pizza = 0
        qty_pepsi = 0
        if "yes" in qty:
            talk("Would you like to increase the quantity of pizza?")
            wh_qty = rec_audio()
            if "yes" in wh_qty:
                talk("How many more pizzas would you like to add? ")
                try:
                    qty_pizza = rec_audio()
                    qty_pizza = int(qty_pizza)
                    if qty_pizza > 0:
                        talk_piz = f"Adding {qty_pizza} more pizzas"
                        talk(talk_piz)
                        for i in range(qty_pizza):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]').click()
                except:
                    talk("I dont know that.")
            else:
                pass

            talk("Would you like to increase the quantity of pepsi?")
            pep_qty = rec_audio()
            if "yes" in pep_qty:
                talk("How many more pepsis would you like to add? ")
                try:
                    qty_pepsi = rec_audio()
                    qty_pepsi = int(qty_pepsi)
                    if qty_pepsi > 0:
                        talk_pep = f"Adding {qty_pepsi} more pepsis"
                        talk(talk_pep)
                        for i in range(qty_pepsi):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]').click()
                except:
                    talk("I dont know that.")
            else:
                pass

        elif "no" in qty:
            pass

        total_pizza = qty_pizza + 1
        total_pepsi = qty_pepsi + 1
        tell_num = f"This is your list of order. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
        talk(tell_num)
        check_order = rec_audio()
        if "yes" in check_order:
            talk("Checking out")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button').click()
            sleep(1)
            total = driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[6]/span[2]/span')
            total_price = f'total price is {total.text}'
            talk(total_price)
            sleep(1)
        else:
            exit()

        talk("Placing your order")
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[8]/button').click()
        sleep(2)
        try:
            talk("Saving your location")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input').click()
            sleep(2)
        except:
            talk("The store is currently offline.")
            exit()

        talk("Do you want to confirm your order?")
        confirm = rec_audio()
        if "yes" in confirm:
            talk("Placing your order")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
            sleep(2)
            talk("Your order is placed successfully. Wait for Dominos to deliver your order. Enjoy your day!")
        else:
            exit()

    else:
        exit()

while True :
    try:
        text = rec_audio()
        speak =" "
        if call (text):          #WAKE WORD
            speak = speak + say_hello(text)
            if "date" in text or "day" in text or "month" in text:
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
                speak = speak+" "+"It is"+str(hour)+":"+minute+" "+meridiem+" ."
            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person,sentences=2)
                    speak = speak+" "+wiki
            elif "who are you" in text or "define yourself" in text:
                speak =speak+"""Hello ,Elsa is my name , Helping you is my game. I am here to make your life easier. You can command me to perform various tasks such as solving mathematical questions or opening  applications etcetera """
            elif "your name" in text:
                speak = speak + " my name is elsa"
            elif "who am I" in text:
                speak= speak + "You must probably be a human"
            elif "how are you" in text:
                speak = speak +"I am fine,Thank you for asking.This is a challenging time for us.I hope you and your loved ones are staying safe and healthy."
                speak =speak+"\nHow are you?"
            elif "fine" in text or "good" in text:
                speak =speak + "I am glad to know that you are fine"
            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening google chrome"
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )
                elif "word" in text.lower():
                    speak = speak +"Opening Microsoft Word"
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                    )
                elif "excel" in text.lower():
                    speak =  speak + "Opening Microsoft excel"
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
                elif "vs code" in text.lower():
                    speak =  speak +  " Opening visual studio code"
                    os.startfile(r"E:\Microsoft VS Code\Code.exe")
                elif "youtube" in text.lower():
                    speak = speak + "Opening youtube"
                    webbrowser.open("https://www.youtube.com/")
                elif "google" in text.lower():
                    speak =  speak +"Opening google "
                    webbrowser.open("https://google.com")
                elif "stackoverflow" in text.lower():
                    speak  = speak + "Opening stackoverflow"
                    webbrowser.open("https://stackoverflow.com/")
                elif "meet" in text.lower():
                    speak =  speak + "Opening google meet"
                    webbrowser.open("https://meet.google.com/")
            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" +
                    "+".join(search)
                )
                speak = speak + "Opening " + str(search) + " on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "change background" in text or "change wallpaper" in text:
                img = r'C:\Users\HP\Desktop\wallpaper'
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0,randomImg, 0)
                speak = speak + "Background changed successfully"

            elif "play music" in text or "play song" in text:
                talk("Here you go with music")
                music_dir = r'C:\Users\HP\Desktop\songs'
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                random = os.path.join(music_dir, d)
                playsound.playsound(random)

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "Recycle Bin Emptied"

            elif "make a note" in text or "remember this" in text:
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that."

            elif "joke" in text:
                speak = speak + pyjokes.get_joke()



            elif "where is" in text or "show me" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + "located."
                webbrowser.open(url)

            elif "email to computer" in text or "gmail to computer" in text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    to = "Receiver email address"
                    send_email(to, content)
                    speak = speak + "Email has been sent !"
                except Exception as e:
                    print(e)
                    talk("I am not able to send this email")

            elif "mail" in text or "email" in text or "gmail" in text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    talk("whom should i send")
                    to = input("Enter To Address: ")
                    send_email(to, content)
                    speak = speak + "Email has been sent !"
                except Exception as e:
                    print(e)
                    speak = speak + "I am not able to send this email"

            elif "weather" in text:
                key = "3b57c50c8cebf9a80b93517dd4087080"
                weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                ind = text.split().index("in")
                location = text.split()[ind + 1:]
                location = "".join(location)
                url = weather_url + "appid=" + key + "&q=" + location
                js = requests.get(url).json()
                if js["cod"] != "404":
                  weather = js["main"]
                  temperature = weather["temp"]
                  temperature = temperature - 273.15
                  humidity = weather["humidity"]
                  desc = js["weather"][0]["description"]
                  weather_response = " The temperature in Celcius is " + str(round(temperature, 2)) + " The humidity is " + str(humidity) + " and The weather description is " + str(desc)
                  speak = speak + weather_response
                else:
                    speak = speak + "City Not Found"

            elif "news" in text:
                    url = (
                        "http://newsapi.org/v2/top-headlines?"
                        "country=in&"
                        "apiKey=b9c8b6bc00ac4d8a80bde0fc6e0aef04"
                    )

                    try:
                        response = requests.get(url)
                    except:
                        talk("Please check your connection")

                    news = json.loads(response.text)

                    for new in news["articles"]:
                        print(str(new["title"]), "\n")
                        talk(str(new["title"]))
                        obj.runAndWait()

                        print(str(new["description"]), "\n")
                        talk(str(new["description"]))
                        obj.runAndWait()
                        time.sleep(2)



            elif "send message" in text or 'send a message' in text:
               account_sid = "ACa288e1d737f8fb163ed65e886525d152"
               auth_token = "7ac1faa0d46037bb60ab3a2b24b16529"
               client = Client(account_sid, auth_token)

               talk("What should i send")
               message = client.messages.create(
                 body=rec_audio(), from_="+16205914909", to="9486973639"
               )
               print(message.sid)
               speak = speak + "Message sent successfully"

            elif "calculate" in text:
                app_id = "H5G8WP-YJY5RAKTQJ"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("calculate")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak =  speak + "The answer is " + answer

            elif "what is" in text or "who is" in text:
                app_id = "H5G8WP-YJY5RAKTQJ"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("is")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " +answer

            elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
                talk("for how many seconds do you want me to sleep")
                a = int(rec_audio())
                time.sleep(a)
                speak = speak + str(a) + " seconds completed. Now you can ask me anything"

            elif "exit" in text or "quit" in text:
                exit()

            elif "order a pizza" in text or "pizza" in text:
                pizza()

            response(speak)

    except:
        talk("I don't know that")

