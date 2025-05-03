import time
import requests
from config import Config

class GitHubClient:
    def __init__(self):
        self.token = Config.GITHUB_TOKEN
        self.repo = Config.GITHUB_REPO
        self.base = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def fetch_last_merged_prs(self, count=10):
        url = f"{self.base}/repos/{self.repo}/pulls"
        params = {"state": "closed", "sort": "updated", "direction": "desc", "per_page": count}
        r = requests.get(url, headers=self.headers, params=params)
        r.raise_for_status()
        items = r.json()
        return [pr for pr in items if pr.get('merged_at')]

    def fetch_pr_diff(self, pr_number):
        url = f"{self.base}/repos/{self.repo}/pulls/{pr_number}"
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        return r.json().get("diff_url")

    def download_diff(self, diff_url, retries=3, delay=2):
        for attempt in range(retries):
            r = requests.get(diff_url, headers=self.headers)
            if r.status_code == 429:
                print(f"Rate limit hit. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # exponential backoff
                continue
            r.raise_for_status()
            return r.text
        raise Exception("Failed to download diff after retries.")
