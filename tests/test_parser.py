import pytest
from utils.parser import extract_jira_key, extract_confluence_id

def test_extract_jira_key():
    assert extract_jira_key('fixing bug PROJ-123 now') == 'PROJ-123'
    assert extract_jira_key('no key here') is None

def test_extract_confluence_id():
    assert extract_confluence_id('https://example.atlassian.net/wiki?pageId=456') == '456'
    assert extract_confluence_id('no link') is None