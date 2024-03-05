import requests


def fetch_repo_info(url):
    parts = url.rstrip('/').split('/')
    username, repo_name = parts[-2], parts[-1]
    api_url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(api_url)

    if response.status_code == 200:
        repo_info = response.json()
        branches = fetch_branches(api_url + "/branches")
        contributors = fetch_contributors(api_url + "/contributors")
        languages = fetch_languages(api_url + "/languages")
        commits = fetch_commits(api_url + "/commits")
        issues = fetch_issues(api_url + "/issues")

        repo_info['branches'] = len(branches)
        repo_info['contributors'] = len(contributors)
        repo_info['languages'] = languages
        repo_info['commits'] = len(commits)
        repo_info['issues'] = len(issues)

        return repo_info
    else:
        return None


def fetch_branches(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_contributors(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_languages(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def fetch_commits(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_issues(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def print_repo_info(repo_info):
    print("\033[1m" + "Repository Information:" + "\033[0m")
    print(f"\033[94mRepository Name:\033[0m {repo_info['full_name']}")
    print(f"\033[94mDescription:\033[0m {repo_info['description']}")
    print(f"\033[94mURL:\033[0m {repo_info['html_url']}")
    print(f"\033[94mLanguage:\033[0m {repo_info['language']}")
    print(f"\033[94mDefault Branch:\033[0m {repo_info['default_branch']}")
    print(f"\033[94mCreated At:\033[0m {repo_info['created_at']}")
    print(f"\033[94mUpdated At:\033[0m {repo_info['updated_at']}")
    print(f"\033[94mSize:\033[0m {repo_info['size']} KB")
    print(f"\033[94mStars:\033[0m {repo_info['stargazers_count']}")
    print(f"\033[94mForks:\033[0m {repo_info['forks_count']}")
    print(f"\033[94mOpen Issues:\033[0m {repo_info['open_issues_count']}")
    print(f"\033[94mBranches:\033[0m {repo_info['branches']}")
    print(f"\033[94mContributors:\033[0m {repo_info['contributors']}")
    print("\033[94mLanguages:\033[0m")
    for language, percentage in repo_info['languages'].items():
        print(f"  - {language}: {percentage}%")
    print(f"\033[94mCommits:\033[0m {repo_info['commits']}")


def main():
    url = input("Enter the GitHub repository URL: ")
    repo_info = fetch_repo_info(url)

    if repo_info:
        print_repo_info(repo_info)
    else:
        print("Failed to fetch repository information.")


if __name__ == "__main__":
    main()
