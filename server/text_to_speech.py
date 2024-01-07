from gtts import gTTS
from playsound import playsound
import os, ntpath, posixpath, shutil

TTS_OUTPUT = "TTS.mp3"

def google_tts(input_text, language): 
    """
    Takes a string and an IETF tag to convert into speech. Generates an audio file at TTS_OUTPUT

    @param input_text: Text in a certain language

    @param language: IETF tag of the language for input_text
    """
    myobj = gTTS(text=input_text, lang=language, slow=False)
    myobj.save(TTS_OUTPUT)
    playsound(TTS_OUTPUT)

def upload_tts(client_ip):
    dest = posixpath.join(client_ip, 'universal_translator', 'cache', "TTS.mp3")
    shutil.copy(TTS_OUTPUT, dest)

def main():
    text = "the quick brown fox jumped over the lazy dog"
    language = "en"
    
    google_tts(text, language)
    playsound(TTS_OUTPUT)



if __name__ == "__main__":
    main()
