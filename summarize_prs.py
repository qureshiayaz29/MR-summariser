import os

import time
import github_client
from utils.parser import extract_jira_key, extract_confluence_id
from github_client import GitHubClient
from jira_client import JiraClient
from confluence_client import ConfluenceClient
from chatgpt_client import ChatGPTClient

OUTPUT_FILE = os.getenv("SUMMARY_OUTPUT", "pr_summaries.txt")

def main():
    gh = GitHubClient()
    jira = JiraClient()
    conf = ConfluenceClient()
    ai = ChatGPTClient()

    prs = gh.fetch_last_merged_prs(count=10)
    print('processing...')
    with open(OUTPUT_FILE, 'w') as f:
        for pr in prs:
            try:
                number = pr['number']
                title = pr['title']
                url = pr['html_url']
                user = pr['user']['login']
                body = pr.get('body', '')

                jira_key = extract_jira_key(body)
                jira_data = jira.fetch_issue(jira_key) if jira_key else {}
                conf_id = extract_confluence_id(body) or (jira_data.get('description') and extract_confluence_id(jira_data['description']))
                conf_text = conf.fetch_page(conf_id) if conf_id else ''

                diff_url = gh.fetch_pr_diff(number)
                diff_text = gh.download_diff(diff_url)

                context = f"JIRA: {jira_data.get('summary','')}"
                summary = ai.summarize_diff(diff_text[:2000], context)

                f.write(f"PR #{number}: {title} by {user}\n")
                f.write(f"URL: {url}\n")
                if jira_key:
                    f.write(f"JIRA: {jira_key} - {jira_data.get('summary')}\n")
                if conf_id:
                    f.write(f"Confluence excerpt: {conf_text[:200]}\n")
                f.write("Summary:\n" + summary + "\n")
                f.write("="*80 + "\n\n")

                time.sleep(2)  # Delay to reduce chance of rate-limiting
            except Exception as e:
                print(f"Error processing PR #{pr['number']}: {e}")
    print('pr summary generated: ', OUTPUT_FILE, ' Repo: ', github_client.Config.GITHUB_REPO)

if __name__ == '__main__':
    main()