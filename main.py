from clone_all.clone_all import clone_all

if __name__ == '__main__':
    directory = None  # directory where all the projects will be stored
    skip_pull = True  # if true, script will only clone new repos and not pull existing repos
    clone_all(directory=directory, skip_pull=skip_pull)
