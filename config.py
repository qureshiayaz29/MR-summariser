import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Public GitHub repository (e.g., "owner/repo")
    GITHUB_REPO = os.getenv("GITHUB_REPO")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    JIRA_USER = os.getenv("JIRA_USER")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
    JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")

    CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")
    CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL")

    # OpenAI API
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
