import os
from openai import OpenAI

API_KEY = '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'

def get_chatbot_response(message):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=API_KEY,
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model="gpt-3.5-turbo",
        )
        output = chat_completion.message.content
    except:
        output = "Error in OpenAI API."

    return output
