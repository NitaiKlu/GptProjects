"""
This file consists of the implementation of the class PromptRunner. 
This class rcvs text in natural language that we call a "command". It then creates
a "prompt" to be run by chatGPT according to the command. It also runs the 
prompt and sends back the response object.

The PromptRunner saves statistics and history of the run both for a specific
conversation with the chat (instance of this class), and for the entire runs 
performed so far. 

TODO
1. add return codes for better error handling
2. parse commands into prompts (low priority)

"""
# importing the API of chatGPT
import openai

# the PromptRunner class
class PromptRunner:
    # PromptRunner class variables - history of all runs and general info needed
    # the file on my comp that holds the secret key
    apiFile = open("C:\\Users\\nitai\\Technion\\key.txt", "r")
    # get the apiKey from the file
    apiKey = apiFile.read()
    # update the module about the key
    openai.api_key = apiKey
    # number of instances of this class ever created
    numberOfRuns = 0
    # number of tokens (prompt + response) that all instances used so far
    numberOfTokens = 0
    # number of prompts that all instances asked from the chatGPT so far
    numberOfPrompts = 0

    # regular c'tor of the instance of a promptRunner
    def __init__(self, maxTokensResponse=20, maxTokensPrompt=20) -> None:
        # member of the maximum length of a response
        self.m_maxTokensResponse = maxTokensResponse
        # member of the maximum length of a prompt
        self.m_maxTokensPrompt = maxTokensPrompt
        # member of the history of the conversation
        self.m_conversation = []
        # class variables update
        PromptRunner.numberOfRuns += 1

    # the main function that recvs a command and returns the response of
    # chatGPT to that command
    def runCommand(self, command):
        # parse to a prompt
        prompt = self.createPrompt(commandToParse=command)

        # check the prompt follows the instance conditions
        if (self.isPromptTooLong(prompt=prompt)):
            # TODO make this more relevant, maybe with exceptions or RC
            return "error: Cannot create a response. The prompt is too long"

        # generate the response from chatGPT
        response = openai.Completion.create(
            engine="text-davinci-001", prompt=prompt, max_tokens=30)

        # methods update - add to history of this conversation
        self.m_conversation.append(response)

        # class variables update
        PromptRunner.numberOfPrompts += 1
        PromptRunner.numberOfTokens += response.usage.total_tokens

        return response

    # parse a command in natural language to a prompt to be run over chatGPT
    def createPrompt(self, commandToParse):
        return commandToParse

    # STATIC: gets a text and estimates the number of tokens used in the text
    @staticmethod
    def estimateTokens(text):
        # count the number of words in the text
        wordCount = len(text.split())
        # count the number of characters in the prompt
        charCount = len(text)
        # estimation of tokens using words
        tokensCountWordEst = wordCount / 0.75
        # estimation of tokens using characters
        tokensCountCharEst = charCount / 4.0
        # find the max of the two estimations
        output = max(tokensCountWordEst,tokensCountCharEst)
        return output
    
    # recvs a prompt and returns True if it's too long to be handled according
    # to self's attributes. False otherwise
    def isPromptTooLong(self, prompt):
        numberOfTokens = PromptRunner.estimateTokens(prompt)
        if(numberOfTokens > self.m_maxTokensPrompt):
            return True
        return False

    # get the max number of tokens in a response of the chatGPT
    def getMaxTokensResponse(self):
        return self.m_maxTokensResponse
    
    # get the max number of tokens in a prompt of the chatGPT
    def getMaxTokensResponse(self):
        return self.m_maxTokensPrompt 

    # update the max number of tokens in a response of the chatGPT
    def setMaxTokensResponse(self, maxTokensResponse):
        self.m_maxTokensResponse = maxTokensResponse

    # update the max number of tokens in a prompt of the chatGPT
    def setMaxTokensPrompt(self, maxTokensPrompt):
        self.m_maxTokensPrompt = maxTokensPrompt
    
    # get the number of tokens used by all instances so far
    @classmethod
    def getMaxTokensResponse(cls):
        return cls.numberOfTokens
    
    # get the number of prompts activated so far by all instances
    @classmethod
    def getMaxTokensResponse(cls):
        return cls.m_maxTokensPrompt 

