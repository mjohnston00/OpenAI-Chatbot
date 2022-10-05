import os
import openai

with open("key.txt") as f:
    key = f.read().strip()
    openai.api_key = key

def getUserPrompt():
    prompt = ""
    while len(prompt)==0:
        prompt = input(">>>")
    return prompt

while True:
    userPrompt = getUserPrompt()
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=userPrompt,
        temperature=0.25,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[]
    )
    responseText = response.choices[0].text
    print("\nOpenAI:"+responseText)
