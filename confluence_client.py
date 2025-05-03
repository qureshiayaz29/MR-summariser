import requests
from config import Config

class ConfluenceClient:
    def __init__(self):
        self.base = Config.CONFLUENCE_BASE_URL
        self.headers = {"Authorization": f"Bearer {Config.CONFLUENCE_API_TOKEN}"}

    def fetch_page(self, page_id):
        url = f"{self.base}/wiki/rest/api/content/{page_id}?expand=body.storage"
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        data = r.json()
        return data.get("body", {}).get("storage", {}).get("value")