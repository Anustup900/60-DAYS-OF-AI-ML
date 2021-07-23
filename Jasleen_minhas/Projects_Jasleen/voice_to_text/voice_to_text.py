import speech_recognition as sr

recognizer = sr.Recognizer()

# Recording the sound

with sr.Microphone() as source:
    # print("Adjusting noise")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("\n\nRecording.....")
    recorded_audio = recognizer.listen(source, timeout=10)
    print("Done recording\n\n")


# Recorgnizing the Audio 

try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
    print("\nDecoded Text : {}\n\n".format(text))

except Exception as ex:
    print(ex)