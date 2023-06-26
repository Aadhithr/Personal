from __future__ import print_function
import datetime
import pickle
import os.path
import os
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess
import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


# to search
# print(chatbot_query('how old is samuel l jackson'))

def chatbot_query(query, index=0):
    fallback = 'Sorry, I cannot think of a reply for that.'
    result = ''

    try:
        search_result_list = list(search(query, tld="co.in", num_results=10))

        page = requests.get(search_result_list[index])

        tree = html.fromstring(page.content)

        soup = BeautifulSoup(page.content, features="lxml")

        article_text = ''
        article = soup.findAll('p')
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text = True))
        article_text = article_text.replace('\n', '')
        first_sentence = article_text.split('.')
        first_sentence = first_sentence[0].split('?')[0]

        chars_without_whitespace = first_sentence.translate(
            { ord(c): None for c in string.whitespace }
        )

        if len(chars_without_whitespace) > 0:
            result = first_sentence
        else:
            result = fallback

        speak(result)
    except:
        if len(result) == 0: result = fallback
        speak(result)

WAKE = "okay"


print("Start")


while True:
    print("listening...")
    text = get_audio()

    if text.count(WAKE) > 0:
        speak("Hello Aadhith")
        text = get_audio()


    NOTE_STR = ["make a note", "write this down", "remeber this", "note this"]
    for phrase in NOTE_STR:
        if phrase in text:
            speak("What would you like me to write down?")
            note_text = get_audio()
            note(note_text)
            speak("I've made a note of that.")

    NAME_STR = ["what is my name", "could you tell me my name", "do you know my name"]
    for phrase in NAME_STR:
        if phrase in text:
            speak("Hello, your name is Aadhith")

    QUESTION_STR = ["i have a question", "can you clear my doubt"]
    for phrase in QUESTION_STR:
        if phrase in text:
            speak("Please say your question")
            Question = get_audio()
            chatbot_query(Question)

        



