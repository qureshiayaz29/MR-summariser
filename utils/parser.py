import re

def extract_jira_key(text):
    m = re.search(r"([A-Z]+-\d+)", text)
    return m.group(1) if m else None

def extract_confluence_id(text):
    m = re.search(r"pageId=(\d+)", text)
    return m.group(1) if m else None
