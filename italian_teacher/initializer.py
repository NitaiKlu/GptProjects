"""
this file consists of the implementation of the Initializer class. 
the class is responsible to initialize a conversation according to what the
user specified. 

This initialization is basically just sending the first few commands to the chat
so that it "knows" which types of prompts it'll get, and which answers it should supply. 

The different types of initialization are equivalent to the modes of the Teacher:
1. Italian Conversation:
    a. level of Italian vocabulary
    b. time tenses that the chat will use
    c. length of the answers
    d. topics to talk about
    e. how pedant the chat is with mistakes 

2. Grammer Teacher:
3. Unseen Exam:
4. Translator: 

"""

class Initializer:
    # c'tor that doesn't do much. the other functions in the API
    # will be the ones the user uses to initialize his conversation
    def __init__(self, promptRunner, maxTokensToUse = 100) -> None:
        # maximal number of tokens that the initializer should use to initialize
        self.m_maxTokensToUse = 100
        # a list containing the strings of the commands that the initializer used
        self.m_commands = []
        # the promptRunner instance that is running the prompts of the initializer 
        self.m_promptRunner = promptRunner
    
    # a long function documentation that explains about the options of each 
    # function parameter. This function returns a bool val of True if the 
    # initiation succeeded or not
    def initConversation(self, numOfWordsInAnswer = "30") -> bool:
        # general Italian Conversation prompts
        successResult = self.runAndValidate("from now on talk in italian until I say \"stop\" or if I ask you a question in english")
        if successResult == False:
            pass
        
        # set mistakes correction
        successResult = self.runAndValidate("Whenever I make a mistake in Italian you correct me with an explanation. ")
        if successResult == False:
            pass

        # setting vocab level of the chat
        # setting the maximal number of words in the response
        successResult = self.runAndValidate("Speak basic italian and don't use very difficult vocabulary. Your answers shouldn't be more than" + str(numOfWordsInAnswer) + "words long")
        if successResult == False:
            pass

    def initGrammerTeacher(self, manyManyArgs):
        pass

    def initUnseenExam(self, manyManyArgs):
        pass

    def initTranslator(self, manyManyArgs):
        pass

    # validate that the response arrived and didn't stop due to max tokens limit,
    # API key expiration, too long of an answer or network issues
    @staticmethod
    def validateResponse(responseToValidate) -> bool:
        pass
    
    # run the command using m_promptRunner and validate that the answer makes
    # sense
    def runAndValidate(self, promptToRun) -> bool:
        # run the prompt over the chat
        response = self.m_promptRunner.runCommand(promptToRun)
        # validate the response and return the answer
        return Initializer.validateResponse(responseToValidate=response)
