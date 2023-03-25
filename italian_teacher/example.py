"""
This file contains the first example, just to try the AI out. 
"""
import os
import openai

API_KEY = "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"

openai.api_key = API_KEY
prompt = " write a very short joke."

response = openai.Completion.create(
    engine="text-davinci-001", prompt=prompt, max_tokens=30)

print(response)
