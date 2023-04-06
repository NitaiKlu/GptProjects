"""
This file contains the implementation of the server of the Italian teacher.
The server gets commands from the user and responds accordingly. 
At first the commands are very specific and they are setting up the environment of the
app. Later, the commands can vary as chatGpt is actually the brain behins the server's
responses. 

The usage of the server to generate an instance of any mode is as following: 
1. start with...
2.
3.

"""
import sys
import os
sys.path.append(os.getcwd())
from whisperer import Whisperer
from initializer import Initializer
from promptRunner import PromptRunner

# the class that is receiving the commands from the client and responses accordingly.


class Server:
    def __init__(self, mode="conversation", maxTokensPrompt=100,
                 maxTokensResponse=100) -> None:
        self.m_mode = mode
        self.m_promptRunner = PromptRunner(maxTokensPrompt, maxTokensResponse)
        self.m_initializer = Initializer(self.m_promptRunner)
        self.m_whisperer = Whisperer()

        # init the chat according to the mode specified
        if self.m_mode.lower() == "conversation":
            self.m_initializer.initConversation()

        elif self.m_mode.lower() == "grammer":
            self.m_initializer.initGrammerTeacher()

        elif self.m_mode.lower() == "translator":
            self.m_initializer.initTranslator()

        elif self.m_mode.lower() == "unseen":
            self.m_initializer.initUnseenExam()
    
    def startConversation(self):
        # cute starting message
        self.m_whisperer.textToAudio("Ciao! Mi chiamo chat GPT. Che piacere parlare con te!", language='italian')
        language = 'italian'
        # the conversation instance
        while True:
            userCommand = self.getAudioCommand(language=language) # listen to the user's speech

            if userCommand == "basta" or userCommand == "stop": # the user wants to stop
                self.m_whisperer.textToAudio("Arivaderci!", language='italian')
                break
            elif userCommand == "error_in_speech": # the audio of the user wasn't clear
                print("Trying again in 2 seconds...")
                self.m_whisperer.wait(2)
                continue

            response = self.runTextCommand(userCommand) # chat responses as text

            self.m_whisperer.textToAudio(response.choices[0].text, language=language) # chat response out loud

            inputStr = input("Type 'en'/'it' to change languages. Anything else to continue:\n").strip() # user times the next audio
            if inputStr == 'en':
                language = 'english'
            if inputStr == 'it':
                language = 'italian'

    def runTextCommand(self, command):
        # run the command 
        response = self.m_promptRunner.runCommand(command=command)
        return response

    def getAudioCommand(self, language):
        # parse the audio input into text
        userCommand = self.m_whisperer.audioToText(language=language) 
        return userCommand
