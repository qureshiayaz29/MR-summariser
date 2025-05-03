import pytest
from chatgpt_client import ChatGPTClient
from unittest.mock import patch

@patch('openai.ChatCompletion.create')
def test_summarize_diff(mock_create):
    mock_create.return_value.choices = [type('c', (), {'message': type('m', (), {'content': 'test summary'})})]
    client = ChatGPTClient()
    assert client.summarize_diff('diff text', 'context') == 'test summary'
