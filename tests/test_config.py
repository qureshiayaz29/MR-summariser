import os

def main():
    github_repo = os.getenv("GITHUB_REPO")
    if github_repo:
        print(f"GITHUB_REPO is set to: {github_repo}")
    else:
        print("GITHUB_REPO is not set.")

if __name__ == '__main__':
    main()