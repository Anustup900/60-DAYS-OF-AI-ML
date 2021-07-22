#!/usr/bin/env python
# coding: utf-8

# In[13]:


import speech_recognition as sr


# In[14]:


filename = "namaste.mp3"


# In[15]:


# initialize the recognizer
r = sr.Recognizer()


# In[22]:


with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)


# In[ ]:




