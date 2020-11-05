import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def PietraSays(message):
    language = 'en' # Set your language here (ex: pt-br, en, es, de).
    myobj = gTTS(text=message, lang=language, slow=False) # Generating Text To Speech Function.
    myobj.save("Voice.mp3") # Saving the audio data.
    playsound.playsound("Voice.mp3", True)
    os.remove("Voice.mp3") # Removing the current audio data to be possible Pietra speak again.
PietraSays("Hello, i am pietra. How can i help you?")

r = sr.Recognizer()

def UserSpeak():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        Recording = "Pietra is Listening..."
        global audio
        print(Recording)
        audio = r.listen(source)
    try:
        global phrase
        phrase = r.recognize_google(audio, language="en")
        print("You said: " + phrase)
    except LookupError:
        print("Pietra couldn't recongize your voice.")
UserSpeak()

if(phrase == "Pietra remember this"):
    PietraSays("What i need to know? ")
    UserSpeak()
    PietraSays("Okay, i will remember that")