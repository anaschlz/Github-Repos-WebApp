from flask import Flask, render_template, request
import requests

class GitHubApp:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/', methods=['GET', 'POST'])
        def index():
            if request.method == 'POST':
                username = request.form['username']
                response = requests.get(f'https://api.github.com/users/{username}/repos')
                if response.status_code == 200:
                    data = response.json()
                    repo_names = [repo['name'] for repo in data]
                    repo_count = len(repo_names)
                    return render_template('index.html', repo_names=repo_names, repo_count=repo_count)
                else:
                    return render_template('index.html', error='Usuário não encontrado')
            return render_template('index.html')

    def run(self):
        self.app.run(debug=True, host='127.0.0.1', port=8000)

if __name__ == '__main__':
    github_app = GitHubApp()
    github_app.run()
