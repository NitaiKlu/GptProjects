"""
This file contains the first example, just to try the AI out. 
"""
import sys
import os
sys.path.append(os.getcwd())
from promptRunner import PromptRunner


firstPromptRunner = PromptRunner(maxTokensPrompt=40, maxTokensResponse=30)
response = firstPromptRunner.runCommand("Write that this is a test.")
print(response)
print(response.choices[0].text)
