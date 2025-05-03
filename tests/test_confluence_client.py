import pytest
from confluence_client import ConfluenceClient
from unittest.mock import patch

def test_fetch_page(monkeypatch):
    data = {'body': {'storage': {'value': 'Content'}}}
    monkeypatch.setattr('confluence_client.requests.get', lambda *args, **kwargs: type('r', (), {'json': lambda: data, 'raise_for_status': lambda: None}))
    client = ConfluenceClient()
    assert client.fetch_page('123') == 'Content'