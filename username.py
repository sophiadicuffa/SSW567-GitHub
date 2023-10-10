import urllib.request
import json

def fetch_data_from_github(user_id):
    url = f"https://api.github.com/users/{user_id}/repos"
    response = urllib.request.urlopen(url)
    data = json.load(response)
    return data

def count_commits(user_id, repo_name):
    commit_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    commit_response = urllib.request.urlopen(commit_url)
    commit_data = json.load(commit_response)
    return len(commit_data)

def get_user_repositories_with_commits(user_id):
    data = fetch_data_from_github(user_id)
    repositories = []

    for repo in data:
        repo_name = repo['name']
        num_commits = count_commits(user_id, repo_name)
        repositories.append({"Repo": repo_name, "Number of commits": num_commits})

    return repositories

user_id = input("Enter GitHub user ID: ")
repos_with_commits = get_user_repositories_with_commits(user_id)

for repo in repos_with_commits:
    print(f"Repo: {repo['Repo']} Number of commits: {repo['Number of commits']}")
