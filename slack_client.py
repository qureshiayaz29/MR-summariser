from slack_sdk import WebClient
from config import Config

class SlackClient:
    def __init__(self):
        self.client = WebClient(token=Config.SLACK_BOT_TOKEN)
        self.channel = Config.SLACK_CHANNEL

    def post_message(self, blocks):
        return self.client.chat_postMessage(channel=self.channel, blocks=blocks)
