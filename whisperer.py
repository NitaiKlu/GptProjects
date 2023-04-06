"""
This file contains the implementation of the Whisperer class. 
This class takes audio files and generates text, and the opposite. 
Its functions are all static since there is no difference in its operations from 
one instance to the other.
"""
import speech_recognition as sr # speech recognition converts audio to text
from gtts import gTTS           # GTTS converts text into audio
from pydub import AudioSegment  # to deal with audio files easily
import os                       # os for activating speakers and dealing with file creation and deletion
import time                     # allows to sleep when the speakers activate the audios

# The Whisperer class that converts: audio <--> text
class Whisperer:
    recognizer = sr.Recognizer() # the class's instance of the speech recognizer
    ctr = 0 # number of uses 

    # this methid opens the microphone and listens. Then it prints and returns the result of the speech recognition
    # language: the language of the audio
    @staticmethod
    def audioToText(language) -> str:
        with sr.Microphone() as source:
            print("Speak something:")
            # listeting to user
            audio = Whisperer.recognizer.listen(source)
            print("Collecting information...")
            try:
                # get the code of the language for the Google service
                language = Whisperer.getLanguageCode(language=language)
                # convert the audio to text
                text = Whisperer.recognizer.recognize_google(audio, language=language)
                print("You said: " + text)
                Whisperer.ctr += 1 # update the number of uses
                return text
            except sr.UnknownValueError:
                print("Could not understand audio")
                return "error_in_speech"
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                return "error_in_speech"

    # this method converts the given text (parameter) to an audio file and then plays it and deletes the audio. 
    # to save the audio, specify 'toSave = True' and the path, name of the file under 'pathToBeSaved = <path>', 'fileName = <name>' 
    @staticmethod
    def textToAudio(text, language = 'english', toSave = False, pathToBeSaved = os.getcwd(), fileName = 'audioFile_'):
        lang = Whisperer.getShortLanguageCode(language=language) # get language code

        tts = gTTS(text=text, lang=lang)  # Create gTTS object with text and language

        fullName = pathToBeSaved + "\\" + fileName  + str(Whisperer.ctr) + ".mp3" # The name of the file including path

        tts.save(fullName)  # Save audio file

        mp3_file = AudioSegment.from_file(fullName, format="mp3")
        lengthSeconds = len(mp3_file) / 1000 # length of the audio in seconds

        os.system(fullName)  # Play audio file

        Whisperer.ctr += 1 # update the number of uses

        time.sleep(lengthSeconds + 1) # sleep so that the user hears all of the voice message
        
        # if we're not saving this file
        if toSave == False:  
            os.remove(fullName)

    # gets a language in natural language and returns its "code" in the Google Speech Recognition service. 
    # english -> en-EN
    # Hebrew -> he-HE
    @staticmethod
    def getLanguageCode(language='english') -> str:
        # get both lower and upper caps
        lowerLanguage = language.lower()
        upperLanguage = language.upper()
        # cut to get the the first two letters only
        firstTwoLettersLower = lowerLanguage[:2]
        firstTwoLettersUpper = upperLanguage[:2]
        # concat and return
        return firstTwoLettersLower + '-' + firstTwoLettersUpper
    
    # gets a language in natural language and returns its "code" in the gTTS system 
    # english -> en
    # Hebrew -> he
    @staticmethod
    def getShortLanguageCode(language='english') -> str:
        # get both lower caps
        lowerLanguage = language.lower()
        # cut to get the the first two letters only
        return lowerLanguage[:2]
    
    @staticmethod
    def wait(seconds) -> None:
        time.sleep(secs=seconds)

