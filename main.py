import speech_recognition as sr
from time import ctime
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()


def rupi_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def record_audio(ask=False):

    with sr.Microphone() as source:
        if(ask):
            rupi_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            rupi_speak('Sorry i did not get that')
        except sr.RequestError:
            print('Sorry My Speech service is down')
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        rupi_speak('My name is Rupi')
    if 'what time is it' in voice_data:
        rupi_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        rupi_speak('here is what i found for ' + search)
    if 'find location' in voice_data:
        search = record_audio('What is location name?')
        url = 'https://google.com/maps/place/' + search + '/&%amp;'
        webbrowser.get().open(url)
        rupi_speak('Here is the location of ' + search)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
while 1:
    rupi_speak('How can i help you ')
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
