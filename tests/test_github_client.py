import pytest
from github_client import GitHubClient
from unittest.mock import patch

@patch('github_client.requests.get')
def test_fetch_last_merged_prs(mock_get):
    mock_get.return_value.json.return_value = [
        {"number": 1, "merged_at": "2025-05-01T00:00:00Z"},
        {"number": 2, "merged_at": None}
    ]
    mock_get.return_value.raise_for_status = lambda: None
    gh = GitHubClient()
    result = gh.fetch_last_merged_prs(count=2)
    assert len(result) == 1
