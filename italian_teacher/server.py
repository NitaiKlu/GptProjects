"""
This file contains the implementation of the server of the Italian teacher.
The server gets commands from the user and responds accordingly. 
"""
import sys
import os
sys.path.append(os.getcwd())
from whisperer import Whisperer
from initializer import Initializer
from promptRunner import PromptRunner

# the class that is receiving the commands from the client and responses accordingly.


class Server:
    stopPrompts = ["basta", "quit", "stop", "exit"]
    english = ["en", "english", "eng"]
    italian = ["it", "italian"]
    def __init__(self, mode="conversation", maxTokensPrompt=100,
                 maxTokensResponse=100) -> None:
        self.m_mode = mode
        self.m_promptRunner = PromptRunner(maxTokensPrompt, maxTokensResponse)
        self.m_whisperer = Whisperer()
        # self.m_initializer = Initializer(self.m_promptRunner)

        # init the chat according to the mode specified
        # if self.m_mode.lower() == "conversation":
        #     self.m_initializer.initConversation()

        # elif self.m_mode.lower() == "grammer":
        #     self.m_initializer.initGrammerTeacher()

        # elif self.m_mode.lower() == "translator":
        #     self.m_initializer.initTranslator()

        # elif self.m_mode.lower() == "unseen":
        #     self.m_initializer.initUnseenExam()
    
    def startConversation(self):
        # cute starting message
        self.m_whisperer.textToAudio("Ciao! Mi chiamo chat GPT. Che piacere parlare con te!", language='italian')
        language = 'italian'
        # the conversation instance
        while True:
            userCommand = self.getAudioCommand(language=language) # listen to the user's speech

            if userCommand.lower() in Server.stopPrompts: # the user wants to stop
                self.m_whisperer.textToAudio("Arivaderci!", language='italian')
                break
            elif userCommand.lower() == "error_in_speech": # the audio of the user wasn't clear
                print("Couldn't understand. Trying again in 2 seconds...")
                self.m_whisperer.wait(2)
                continue

            response = self.runTextCommand(userCommand) # chat responses as text

            self.m_whisperer.textToAudio(response.choices[0].text, language=language) # chat's response out loud

            inputStr = input("Type 'en'/'it' to change languages. Anything else to continue:\n").strip() # user times the next audio
            if inputStr in Server.english:
                language = 'english'
            if inputStr in Server.italian:
                language = 'italian'
            if inputStr in Server.stopPrompts:
                break

    def startUnseen(self):
        # topic choice and running the prompt:
        while True:
            topic = input("Type a subject that you want to here a story about. Press enter for random topic, exit to quit:").strip()
            if topic == "": # random topic
                response = self.runTextCommand("Tell me a short story in basic italian.")
            if topic == "exit":
                break
            else: # a specific topic
                cmd = "Tell me a short story in basic italian. Make it about " + topic + ". Make it 100 words long."
                response = self.runTextCommand(cmd)
        # ***************************************************
        # printing the story and saving as mp3 file:
            print("Calculating your story...")
            toReadAgain = True
            fileName = "story_about_" + topic + "_"
            print(response.choices[0].text)
            fileName = self.m_whisperer.textToAudio(response.choices[0].text, language="italian", 
                                                    toSave=True, fileName=fileName) # chat's response out loud
            # ***************************************************
            # will read over and over until user says otherwise:
            while toReadAgain: 
                while True:
                    answer = input("Play one more time? [y/n]: ") 
                    if answer == "n":
                        toReadAgain = False
                        os.remove(fileName)
                        break
                    elif answer == "y":
                        self.m_whisperer.playAudio(fileName=fileName)
                        break
                    elif answer != "y":
                        print("illegal response.\n")

    def runTextCommand(self, command):
        # run the command 
        response = self.m_promptRunner.runCommand(command)
        return response

    def getAudioCommand(self, language):
        # parse the audio input into text
        userCommand = self.m_whisperer.audioToText(language) 
        return userCommand
