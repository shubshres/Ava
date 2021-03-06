###########################
##   Import Statements   ##
###########################
# import speech recognition package
import speech_recognition
# importing text to speech engine
import pyttsx3
# importing pywhatkit to search youtube
import pywhatkit
# importing built in library date and time
# so user can hear current date/time
import datetime
# import wikipedia library for information
import wikipedia
# importing pyjokes libary for jokes
import pyjokes
# importing google search
import googlesearch
# importing web browser so we can open web browser after searching
import webbrowser
# importing gooleapi to search google
from googleapi import google
# importing beep sound for feedback -- after doing some research, I found that
# winsound does not work on mac, so I decided to use a different package (playsound)
# import winsound
from playsound import playsound

# importing OS to get current working directory
import os

# creating a global variable that will run ava
global run

# Creating a recognizer that will recognize the user voice
listener = speech_recognition.Recognizer()

# initializing the text to speech engine
ava = pyttsx3.init()

# creating a var that will store all of the voices the library pyttsx3 provides
voices = ava.getProperty('voices')
# setting ava's voice to female
ava.setProperty('voice', voices[17].id)

# best is 7 so far, 10 is good female too 17 is probs really the best 25,33 is aight
# 16,18 sound chinese asf
# top choices
    # 17, 33,

# creating a function that will make ava talk
def say(output):
    ava.say(output)
    ava.runAndWait()


# function that will take in the mic input
def mic_input():
    # Try block in case no mic input detected
    try:
        with speech_recognition.Microphone() as input_source:
            print('Listening!')
            # storing path of chime
            sound_path = os.getcwd()
            sound_path = sound_path + "/listening.wav"
            # playing sound
            playsound(sound_path)

            # listening for voice
            voice = listener.listen(input_source)

            # setting var called command that will pass the voice to the google api
            # where google will give the text
            command = listener.recognize_google(voice)

            # checking if ava is detected from user voice
            # changing to command to lowercase to check if ai name was mentioned
            command = command.lower()
            if 'ava' in command:
                # taking out ava's name from the command
                command = command.replace('ava ', '')
                return command
            else:
                return command
    except:
        # if microphone input is not detected print error statement
        print("No Input Detected...")
        pass # python will not do anything when the exception happens
        return('')

def run_ava():
    # calling the mic_input function and storing the mic_input in var called command
    command = mic_input()
    print(command)
    # calling the global run to see if we need to exit ava
    global run

    # commands for ava
    if 'your name' in command:
        say('my name is ayva')
    elif 'who are you' in command:
        say('my name is ayva')
        say('i was created by the brilliant minded and best software engineer in the world, Mr. Shoe bye you Sh resta\
         on Sunday, December fifth, 2021 at two fourty two A M to be his virtual assistant')
    # checking if the user would like to play a song
    # playing a song
    elif 'play' in command:
        global run
        # removing play from the command so we can search for the song
        song_name = command.replace('play', '')
        say('playing' + song_name + ' on youtube')
        pywhatkit.playonyt(song_name)
        print('playing' + song_name + 'on youtube')
        run = False
    # telling time
    elif 'time' in command:
        # calling the current time and getting the string v of the time
        curr_time = datetime.datetime.now().strftime('%I:%M %p')
        say("It is currently "+ curr_time)
    # telling the date - not working right now. BUG: Says wrong date
    elif 'date' in command:
        # calling the current time and getting the string v of the time
        curr_date = datetime.datetime.today().strftime("%m/%d/%Y")
        say("Today is "+ curr_date)
    # searching google for something
    elif 'search for' in command:
        googleThis = command.replace('search for ', '')
        url = "https://www.google.com/search?q={}".format(googleThis)
        webbrowser.open(url)
        run = False
    # opening website
    elif 'open' in command:
        url = command.replace(' dot ', '.')
        if 'open' in command:
            url = command.replace('open ', '')
        url = "https://" + url + "/"
        print(url)
        webbrowser.open(url)
        run = False
    elif 'go to' in command:
        url = command.replace(' dot ', '.')
        url = command.replace('go to ', '')
        url = "https://" + url + "/"
        print(url)
        webbrowser.open(url)
        run = False
    # searching wikipedia for a person's details
    elif 'who is ' in command:
        person = command.replace('who is', '')
        try:
            url = "https://www.google.com/search?q={}".format(person)
            webbrowser.open(url)
            person_info = wikipedia.summary(person, 1)
            say("According to wikipedia " + person_info)
        except:
            say("Could not find information about " + person + " but here is what i found on google")
    # searching wikipedia for what something is
    elif 'what is ' in command:
        what = command.replace('what is', '')
        try:
            url = "https://www.google.com/search?q={}".format(what)
            webbrowser.open(url)
            what_info = wikipedia.summary(what, 1)
            say("According to wikipedia " + what_info)
        except:
            say("Could not find information for what is " + what + " but here is what i found on google")
    # telling a joke
    elif 'joke' in command:
        say(pyjokes.get_joke())
    # closing ava
    elif 'goodbye' in command:
        say("Goodbye.")
        run = False
    elif 'thank' in command:
        say("No Problem!")
        run = False
    elif 'how are you' in command:
        say("I am doing great! Thank you for asking!")
    else:
        say("I didn't quite get that.")

run = True

say("Hello! I am ayva! What can I do for you today?")
while(run == True):
    run_ava()
