#########################################################
##   Packages and Dependencies Used for this Project   ##
#########################################################
# Install Speech Recognition Package for python
# https://pypi.org/project/SpeechRecognition/
# pip install SpeechRecognition

# Install Text-to-Speech Conversion library for python
# https://pypi.org/project/pyttsx3/
# pip install pyttsx3

# Install Audio input/output stream library for python
# https://pypi.org/project/PyAudio/
# pip install PyAudio

# install PythonWhatKit which is a package used to search youtube for python
# pip install pywhatkit
# https://pypi.org/project/pywhatkit/

# install wikipedia
# pip install wikipedia
# https://pypi.org/project/wikipedia/

# install pyjokes, library that has jokes
# pip install pyjokes
# https://pypi.org/project/pyjokes/

###########################
##   Import Statements   ##
###########################
# import speech recognition package
import speech_recognition as sr
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

# creating a global variable that will run ava
global run

# Creating a recognizer that will recognize the user voice
listener = sr.Recognizer()

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
        with sr.Microphone() as input_source:
            print('Listening!')
            voice = listener.listen(input_source)

            # setting var called command that will pass the voice to the google api
            # where google will give the text
            command = listener.recognize_google(voice)

            # checking if ava is detected from user voice
            # changing to command to lowercase to check if ai name was mentioned
            command = command.lower()
            if 'your name' in command:
                say('my name is ayva')
            elif 'ava' in command:
                # taking out ava's name from the command
                command = command.replace('ava', '')
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
    # checking if the user would like to play a song
    # playing a song
    if 'play' in command:
        # removing play from the command so we can search for the song
        song_name = command.replace('play', '')
        say('playing' + song_name)
        pywhatkit.playonyt(song_name)
        print('playing' + song_name)
    # telling time
    elif 'time' in command:
        # calling the current time and getting the string v of the time
        curr_time = datetime.datetime.now().strftime('%I:%M %p')
        say("It is currently "+ curr_time)
    # searching wikipedia for a person's details
    elif 'who is ' in command:
        person = command.replace('who is', '')
        person_info = wikipedia.summary(person, 1)
        say("According to wikipedia " + person_info)
    # searching wikipedia for what something is
    elif 'what is ' in command:
        what = command.replace('what is', '')
        what_info = wikipedia.summary(what, 1)
        say("According to wikipedia " + what_info)
    # telling a joke
    elif 'joke' in command:
        say(pyjokes.get_joke())
    # closing ava
    elif 'goodbye' in command:
        say("Goodbye.")
        run = False
    else:
        say("I didn't quite understand.")

run = True

say("Hello! I am ayva. What can I do for you today?")
while(run == True):
    run_ava()
