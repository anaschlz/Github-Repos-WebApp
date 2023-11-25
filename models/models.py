import requests


class GitHubService:
    @staticmethod
    def get_repos(username):
        response = requests.get(f'https://api.github.com/users/{username}/repos')
        if response.status_code == 200:
            data = response.json()
            repo_names = [repo['name'] for repo in data]
            repo_count = len(repo_names)
            return repo_names, repo_count
        else:
            return None
