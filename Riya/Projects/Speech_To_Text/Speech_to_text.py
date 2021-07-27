# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 17:37:46 2021

@author: riya
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile(r'D:/aud.wav') as source:
    audio_text = r.listen(source)
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting Audio to Text...')
        print(text)
     
    except:
         print('Try again...')
