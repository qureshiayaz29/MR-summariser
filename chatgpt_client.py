import os
from openai import OpenAI

from config import Config

# Initialize the OpenAI client
client = OpenAI(api_key=Config.OPENAI_API_KEY)


class ChatGPTClient:
    def summarize_diff(self, diff_text, context=""):
        prompt = f"Summarize the following code diff:\n{diff_text}\nContext: {context}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a code summarization assistant. But the summary should be for developer, make it crisp and concise."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content
