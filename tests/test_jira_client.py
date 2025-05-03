import pytest
from jira_client import JiraClient
from unittest.mock import patch

def test_fetch_issue(monkeypatch):
    data = {'fields': {'summary': 'Summ', 'description': 'Desc'}}
    monkeypatch.setattr('jira_client.requests.get', lambda *args, **kwargs: type('r', (), {'json': lambda: data, 'raise_for_status': lambda: None}))
    client = JiraClient()
    issue = client.fetch_issue('PROJ-1')
    assert issue['summary'] == 'Summ'
