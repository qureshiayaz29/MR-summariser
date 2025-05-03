# 🔍 Local PR Summarizer

**Local PR Summarizer** is a lightweight tool that fetches the last 10 merged pull requests (PRs) from a public GitHub repository, analyzes the code diffs using OpenAI, and generates summarized insights in a local `.txt` file. It optionally integrates with Jira and Confluence if relevant info is provided in the PR description.

---

## ✨ Features

- ✅ Fetch last 10 merged PRs from a GitHub repo
- 🧠 Uses OpenAI to summarize code diffs
- 📄 Optionally extracts context from Jira tickets and Confluence pages
- 💾 Stores summaries in a clean text file for review
- 🔒 Runs locally with API keys managed securely via `.env`

---

## 🛠 Requirements

- Python 3.8+
- GitHub personal access token (for higher rate limits)
- OpenAI API key
- Optional: Jira and Confluence credentials for enhanced context

---

## 🚀 Usage

Run the script to fetch and summarize the latest merged PRs:

```bash
python summarize_prs.py
```

The summaries will be saved in `pr_summaries.txt`.

---

## 🧪 Running Tests

Run unit tests:

```bash
pytest tests/
```

---

## 📁 Project Structure

```bash
.
├── chatgpt_client.py         # Handles OpenAI summarization
├── github_client.py          # Handles GitHub PR/diff API calls
├── jira_client.py            # (Optional) Jira integration
├── confluence_client.py      # (Optional) Confluence integration
├── summarize_prs.py          # Main runner script
├── config.py                 # Loads env/config values
├── utils/
│   └── parser.py             # Utilities to parse PR descriptions
├── tests/                    # Unit tests
├── requirements.txt
└── .env                      # Your secret keys (excluded from git)
```

---

## 📌 Notes

- Public GitHub repos can be accessed without a token, but rate limits are very low. Use a token to increase API limits.
- The tool trims diffs to ~2000 characters for optimal GPT input length.
- A retry mechanism with exponential backoff is used to handle rate limits from GitHub.

---

## 🧠 Example Output

```
PR #44: Add recipe view screen by johnsmith
URL: https://github.com/owner/repo/pull/44
JIRA: RECIPE-112 - Add recipe UI for desserts
Confluence excerpt: This page outlines the design and API details...
Summary:
- Introduced a new RecipeViewModel and associated UI logic.
- Integrated with the Interactor to fetch recipe data from backend.
...
================================================================================
```

---

## 🚀TODO

- [ ] Support fetching pull/merge requests from both **Bitbucket** and **GitHub**, including **private repositories** using authentication.
- [ ] Enable filtering of merged MRs **based on time period** (e.g., last 3 or 7 days) instead of a fixed count. This aligns better with agile development workflows.
- [ ] Replace local text file output with **Slack messages** or **email notifications** to improve visibility and team collaboration.
- [ ] Schedule the script to run via **cron job** (e.g., weekly or at specific times) to eliminate the need for manual execution.
- [ ] Process only MRs that are **merged into specific branches** such as `master`, `main`, or `develop`.

---

## 📜 License

MIT License – Use freely at your own risk.
