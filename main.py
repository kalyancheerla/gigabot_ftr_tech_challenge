import os
from openai import OpenAI

API_KEY = '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'

client = OpenAI(
    # This is the default and can be omitted
    api_key=API_KEY,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me about Frontier Communications",
        }
    ],
    model="gpt-3.5-turbo",
)
print(f'{chat_completion}')
