#!/usr/bin/env python3

import os

repo_path = "/home/cyprich/Skola/"
repo_name = "/PSA"
repo_url = "https://github.com/cyprich/PSA.git"


def clone_repo(path: str, url: str) -> None:
    os.chdir(path)
    os.system("git clone " + url)


def add_file(path: str, rname: str, fname: str) -> None:
    os.chdir(path + rname)
    os.system("git add " + fname)


def commit_changes(path: str, rname: str, message: str) -> None:
    os.chdir(path + rname)
    os.system('git commit -m "' + message + '"')


def push_git(path: str, rname: str) -> None:
    os.chdir(path + rname)
    os.system("git push")


# clone_repo(repo_path, repo_url)

# file = open(repo_path + repo_name + "/efgh.txt", "w")
# file.write("Nahodny text")
# file.close()

# add_file(repo_path, repo_name, "efgh.txt")

# commit_changes(repo_path, repo_name, "Pridany subor efgh")

# push_git(repo_path, repo_name)
