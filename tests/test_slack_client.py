import pytest
from slack_client import SlackClient
from unittest.mock import patch

def test_post_message(monkeypatch):
    fake_client = type('c', (), {'chat_postMessage': lambda **kwargs: {'ok': True}})()
    monkeypatch.setattr('slack_client.WebClient', lambda token: fake_client)
    client = SlackClient()
    assert client.post_message([])['ok'] is True
