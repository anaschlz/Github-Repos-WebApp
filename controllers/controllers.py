from flask import Flask, render_template, request
from models.models import GitHubService
import os


class GitHubAppController:
    def __init__(self):
        self.app = Flask(__name__, template_folder=os.path.abspath("templates"))
        self.github_service = GitHubService()

        @self.app.route('/', methods=['GET', 'POST'])
        def index():
            if request.method == 'POST':
                username = request.form['username']
                repos_data = self.github_service.get_repos(username)
                if repos_data:
                    repo_names, repo_count = repos_data
                    return render_template('index.html', repo_names=repo_names, repo_count=repo_count)
                else:
                    return render_template('index.html', error='Usuário não encontrado')
            return render_template('index.html')

    def run(self):
        self.app.run(debug=True, host='127.0.0.1', port=8000)

if __name__ == '__main__':
    github_app_controller = GitHubAppController()
    github_app_controller.run()
