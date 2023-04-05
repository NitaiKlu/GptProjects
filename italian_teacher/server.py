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
    def __init__(self, mode="conversation", maxTokensPrompt=20,
                 maxTokensResponse=20) -> None:
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

    def runTextCommand(self, command):
        # some command manipulation ...

        # run the command 
        response = self.m_promptRunner.runCommand(command=command)

        # some response manipulation ...
        return response

    def runAudioCommand(self, audio):
        # parse the audio input into text
        command = self.m_whisperer.audioToText(audio=audio)

        # run the text
        response = self.runTextCommand(command=command)

        # parse response back to audio
        audioResponse = self.m_whisperer.textToAudio(response)

        return audioResponse
