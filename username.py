# Sophia DiCuffa - SSW567 HW 04a "Developing with the Perspective of the Tester in mind"

import urllib.request
import json

def get_user_repositories(user_id):
  
    url = f"https://api.github.com/users/{user_id}/repos"
    response = urllib.request.urlopen(url)
    data = json.load(response)

    repositories = []
    for repo in data:
        repo_name = repo['name']
        commit_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commit_response = urllib.request.urlopen(commit_url)
        commit_data = json.load(commit_response)
        num_commits = len(commit_data)
        repositories.append({"Repo": repo_name, "Number of commits": num_commits})

    return repositories

user_id = input("Enter GitHub user ID: ")
repos_with_commits = get_user_repositories(user_id)

for repo in repos_with_commits:
    print(f"Repo: {repo['Repo']} Number of commits: {repo['Number of commits']}")
