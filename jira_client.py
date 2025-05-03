import requests
from config import Config

class JiraClient:
    def __init__(self):
        self.base = Config.JIRA_BASE_URL
        self.auth = (Config.JIRA_USER, Config.JIRA_API_TOKEN)

    def fetch_issue(self, key):
        url = f"{self.base}/rest/api/3/issue/{key}?fields=summary,description"
        r = requests.get(url, auth=self.auth)
        r.raise_for_status()
        data = r.json()
        fields = data.get("fields", {})
        return {"key": key, "summary": fields.get("summary"), "description": fields.get("description")}
