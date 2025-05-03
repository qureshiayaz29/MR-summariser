import openai
from config import Config

class AzureOpenAIClient:
    def __init__(self):
        openai.api_type = "azure"
        openai.api_base = Config.AZURE_OPENAI_ENDPOINT
        openai.api_version = Config.AZURE_OPENAI_API_VERSION
        openai.api_key = Config.AZURE_OPENAI_KEY
        self.deployment = Config.AZURE_OPENAI_DEPLOYMENT

    def summarize_diff(self, prompt):
        resp = openai.ChatCompletion.create(
            engine=self.deployment,
            messages=[{"role": "system", "content": "You are a code summarization assistant."},
                      {"role": "user", "content": prompt}],
            temperature=0.2
        )
        return resp.choices[0].message.content