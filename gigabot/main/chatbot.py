import os
from openai import OpenAI
from django.conf import settings

API_KEY = settings.CHATGPT_API_KEY

def get_chatbot_response(message):
    client = OpenAI(
        api_key=API_KEY,
    )

    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )
        output = chat_completion.choices[0].message.content
        #print(output)
    except:
        output = "Error in OpenAI API."

    return output
