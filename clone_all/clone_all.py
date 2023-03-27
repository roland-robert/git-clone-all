import json
import os
import time

PATH_TO_HERE = os.getcwd()

def clone_all(directory=None):
    if not directory:
        directory = input(f'Input the directory you want to use (leave empty for default : {os.path.join(PATH_TO_HERE, "all-repos")}:')
        if not directory:
            directory = os.path.join(PATH_TO_HERE, 'all-repos')
        
    f = open(f'{PATH_TO_HERE}/clone_all/git-repos.json')
    repo_dict = json.load(f)
    print(len(repo_dict.values()), 'repos to clone/pull')
    for repo_name, repo_url in repo_dict.items():
        print('Getting', repo_name)
        if os.path.exists(os.path.join(directory, repo_name)):
            print('Pulling', repo_name)
            os.system(f'cd {os.path.join(directory, repo_name)}; git pull; cd {PATH_TO_HERE}')        
        else:
            print('Cloning', repo_name)
            os.system(f'git clone {repo_url} {os.path.join(directory, repo_name)}')        


if __name__ == '__main__':
    clone_all()
