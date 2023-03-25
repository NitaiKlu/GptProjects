"""
This file contains the first example, just to try the AI out. 
"""
from promptRunner import PromptRunner

firstPromptRunner = PromptRunner(maxTokensPrompt=40)
response = firstPromptRunner.runCommand("Write that this is a test.")
print(response.choices[0].text)
