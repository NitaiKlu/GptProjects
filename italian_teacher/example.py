"""
This file contains the first example, just to try the AI out. 
"""
import os
import openai

API_FILE = open("C:\\Users\\nitai\\Technion\\key.txt", "r")
openai.api_key = API_FILE.read()
prompt = " write a very short joke."

response = openai.Completion.create(
    engine="text-davinci-001", prompt=prompt, max_tokens=30)

print(response)
