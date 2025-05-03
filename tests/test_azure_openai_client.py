import pytest
from azure_openai_client import AzureOpenAIClient
from unittest.mock import patch

def test_summarize_diff(monkeypatch):
    fake = type('resp', (), {'choices': [type('c', (), {'message': type('m', (), {'content': 'summary'})})]})
    monkeypatch.setattr('openai.ChatCompletion', 'create', lambda **kwargs: fake)
    client = AzureOpenAIClient()
    assert client.summarize_diff('prompt') == 'summary'