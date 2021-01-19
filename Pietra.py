import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import subprocess
import CreateDB
import wikipedia

def PietraSays(message):
    language = 'en' # Set your language here (ex: pt-br, en, es, de).
    myobj = gTTS(text=message, lang=language, slow=False) # Generating Text To Speech Function.
    myobj.save("Voice.mp3") # Saving the audio data.
    playsound.playsound("Voice.mp3", True)
    os.remove("Voice.mp3") #Removing the current audio data to be possible Pietra speak again.
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


def RememberThis():
    PietraSays("What i need to know? ")
    UserSpeak()
    PietraSays("Okay, i will remember that")
    recordedPhrase = phrase
    PietraSays("Have some Keyword that you want to associate this record?")
    UserSpeak()
    if(phrase == "Yes" or phrase == "yes"):
        PietraSays("Alright, so what is the keyword?")
        UserSpeak()
        keyword = phrase
        PietraSays("Understood, associating Keyword Now.")
        CreateDB.cursor.execute("""
        INSERT INTO Memories(phrase, keyword) VALUES(?,?)
        """, (recordedPhrase, keyword))
        CreateDB.conn.commit()

if(phrase == "Pietra remember this"):
    RememberThis()

def MemoriedPhrase():
    CreateDB.cursor.execute("""SELECT (phrase) FROM Memories WHERE keyword = ?""",(phrase, ))
    PhraseToSay = CreateDB.cursor.fetchone()
    PhraseToSay = PhraseToSay[0]

if(phrase == "Pietra what do you remember"):
    CreateDB.cursor.execute("""
    SELECT COUNT(*) FROM Memories
    """)
    count = CreateDB.cursor.fetchone()
    count = count[0]
    if(count == 0):
        PietraSays("You didn't tell me anything to remember")
        PietraSays("Do you want to me remember something now?")
        UserSpeak()
        if(phrase == "Yes" or phrase == "yes"):
            RememberThis()
    elif(count > 0):
        PietraSays("Well, i remember something!")
        PietraSays("Do you have any keyword associated?")
        UserSpeak()
        if(phrase == "Yes" or phrase == "yes"):
            PietraSays("So Tell me, what is the keyword?")
            UserSpeak()
            CreateDB.cursor.execute("""SELECT (phrase) FROM Memories WHERE keyword = ?""",(phrase, ))
            PhraseToSay = CreateDB.cursor.fetchone()
            PhraseToSay = PhraseToSay[0]
            PietraSays("Ah you said to me:"+ PhraseToSay)

if("Pietra what do you know about" in phrase):
    PietraSays("Let me think for a while...")
    phrase = str(phrase)
    word = phrase.replace('Pietra what do you know about ', "")
    #print(word)
    SearchWiki = wikipedia.summary(word, sentences=2)
    PietraSays(SearchWiki)
        