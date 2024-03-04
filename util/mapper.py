import requests


def fetch_repo_contents(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def print_repo_structure(contents, path="", indent=0):
    for item in contents:
        item_path = path + "/" + item['name'] if path else item['name']
        if item['type'] == 'dir':
            print("\033[94m" + "    " * indent + f"|-- {item['name']}" + "\033[0m")
            sub_url = item['url']
            sub_contents = fetch_repo_contents(sub_url)
            if sub_contents:
                print_repo_structure(sub_contents, item_path, indent + 1)
        else:
            print("\033[92m" + "    " * indent + f"|-- {item['name']}" + "\033[0m")


def main():
    url = input("Enter the GitHub repository URL: ")
    api_url = f"https://api.github.com/repos/{url.split('/')[-2]}/{url.split('/')[-1]}/contents/"
    contents = fetch_repo_contents(api_url)
    if contents:
        print(f"Repository Structure for {url}:")
        print_repo_structure(contents)
    else:
        print("Failed to fetch repository structure.")


if __name__ == "__main__":
    main()
