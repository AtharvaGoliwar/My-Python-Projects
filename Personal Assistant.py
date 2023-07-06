from distutils.log import error
from hashlib import new
from urllib.request import urlopen
import webbrowser
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        global query1
        query1 = ""
        print("processing")
        speak("Processing")
        query1 += r.recognize_google(audio,language="en-in")
        print("tu bola",query1) 
    except Exception:
        print("Firse bol")

def weather():
    #api_key = "Your API key"
    #base_url = "http://api.openweathermap.org/data/2.5/weather?"
    print("Tell me your city name")
    speak("Tell me the city name:")
    takecommand()
    #query1 = input('city name')
    url = "https://www.google.com/search?q="+"weather"+query1 
    response = requests.get(url).content
    #getting data
    soup = BeautifulSoup(response,'html.parser')
    temp = soup.find('div',attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str1 = soup.find('div',attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
        #formating it
    data = str1.split('\n')
    time = data[0]
    sky = data[1]
    print(data)
    #getting all data
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
 
    # getting other required data
    pos = strd.find('Humidity')
    other_data = strd[pos:]

 
    # printing all data
    print("Time: ", time)
    speak("Time is {}".format(time))
    print("Temperature of your city is", temp)
    speak("Temperature in your city is {}".format(temp))
    print("Sky Description: ", sky)
    speak("SKy description {}".format(sky))
    print(other_data)
    speak(other_data)

    #x = response.json()
    '''if response.status_code != '404':
        y=x['main']
        current_temp = y['temp']
        current_pres = y['pressure']
        crrent_humid = y['humidity']
        z = x['weather']
        weather_desc = z[0]['description']
        print(str(current_temp))
        print(str(current_pres))
        print(str(crrent_humid))
        print(weather_desc)
    else:
        print('city not found')'''
    '''print(response.status_code)
    if response.status_code != 404:
   # getting data in the json format
        data = response.json()
   # getting the main dict block
        print(data)
        main = data['main']
   # getting temperature
        temperature = main['temp']
   # getting the humidity
        humidity = main['humidity']
   # getting the pressure
        pressure = main['pressure']
   # weather report
        report = data['weather']
        print(f"{query1:-^30}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")'''


def joke():
    import random
    li = ["A man calls the hotel front desk.... Hello how I may I be of assistance sir?... I NEED YOU TO SEND SOMEONE TO MY ROOM RIGHT AWAY.....Calm down Sir, what seems to be the problem?.....My wife is trying to jump out of the window...Oh that sounds like a personal matter, Im afraid we cannot involve ourselves......Listen here you smartass, the window isnt opening up and thats a maintenance matter!",
    "What do you call a very short person that assists you in your timing? A metrognome",
    "God's personal assistant asks him: I finished the animal you wanted me to do.He replies: Great Work! Let's call it the human.Oh, and one last thing. Add a little toe. Why? It's for the furniture. For the what?Trust me. This is going to be funny.",
    ]
    jo = random.randint(0,len(li)-1)
    speak(li[jo])

def openapp():
    import os
    if 'telegram' in query1.lower():
        os.startfile("C:/Users/Atharva Goliwar/AppData/Roaming/Telegram Desktop/Telegram")
        speak("opening telegram")
        return
    elif 'spotify' in query1.lower():
        os.startfile("C:/Users/Atharva Goliwar/Desktop/Atharva/Spotify.lnk")
        speak("opening spotify")

def news():
    url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
    
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
    speak("Hear are the headlines")
    #response = requests.get(url).content
    #getting data
    #soup = BeautifulSoup(response,'html.parser')
    #listdiv = soup.find('div', attrs={'class': 'wmzpFf  yETrXb Ir3o3e ndj7Ed'}).text
    #print(listdiv)
 
    # getting other required data
    #pos = strd.find('Headlines')
    #other_data = strd[pos:]
    #print(other_data)
    #<h2 class="oOr8M  yETrXb Ir3o3e cS3HJf" jsname="smh91d"><span jscontroller="MfVatf" jsaction="click:KjsqPd" jslog="108423; 3:W251bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtudWxsLCJDQUFxS2dnS0lpUkRRa0ZUUmxGdlNVd3lNSFpOUkZaeFlVZGpVMEpYVm5WTVZXUkRSMmRLU2xScFowRlFBUSJdXQ==" data-n-et="1501" data-n-ca-at="1" data-n-ci-wu="./topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&amp;gl=IN&amp;ceid=IN%3Aen"><a href="./topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&amp;gl=IN&amp;ceid=IN%3Aen" class="wmzpFf  yETrXb Ir3o3e ndj7Ed">Headlines</a></span></h2>
    return


def sendmail():
    import smtplib
    try:
        smtp = smtplib.SMTP("smtp.gmail.com",587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login("atharva.goliwar23@gmail.com","9067354364")
        #takecommand()
        query1 = input("bol")
        smtp.sendmail("atharva.goliwar23@gmail.com","atharva.goliwar23@gmail.com",query1)
        print('email sent successfully')
    except Exception as ex:
        print("something went wrong",ex)
    return

def task():
    url = 'https://trello.com/b/Jw2ykFhR/daily-tasks'
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
    speak("Here are your tasks")
    return




if __name__=='__main__':
    speak("Hello")
    #takecommand()
    query1 = input("enter")
    if 'google' in query1.lower():
        #r1 = sr.Recognizer()
        #with sr.Microphone() as source1:
          #  print("Kya search karna hai?")
           #i = input("abc:")
           # r1.pause_threshold = 2
           #audio1 = r1.listen(source1)
        takecommand()
                
        try:
            #print('searching')
            #query1 = r.recognize_google(audio,language="en-in")
            #print("tu bola ",query1)
            l2 = query1.split('search')
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("google.com/search?q={}".format(l2[1]))
        except Exception:
            print("try again")

    elif '.com' in query1.lower():
        l1 = query1.split(' ')
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open("{}".format(l1[1])) 
    
    elif 'weather' in query1.lower():
        weather()
        
    elif 'me the time' in query1.lower():
        url = "https://www.google.com/search?q="+"time"+"in"+"india"
        response = requests.get(url).content
        #getting data
        soup = BeautifulSoup(response,'html.parser')
        time = soup.find('div',attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        print(time)
        speak(time)

    elif 'me a joke' in query1.lower():
        joke()

    elif 'open telegram' in query1.lower() or 'open spotify' in query1.lower():
        openapp()


    elif 'send mail' in query1.lower():
        sendmail()

    elif 'show my tasks' in query1.lower():
        task()

    elif  'tell me the news' in query1.lower():
        #news()
        a = query1.split(' ')
        print(a)
        if a!=['tell','me','the','news']:
            url = "https://news.google.com/search?q={}&hl=en-IN&gl=IN&ceid=IN:en".format(a[5])
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Here are the headlines")
        else:
            news()

    else:
        print("firse bol")


    

