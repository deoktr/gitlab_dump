#!/usr/bin/env python
import gitlab
import sys
import subprocess
import os
import shutil

gitlab_host = sys.argv[1]
gitlab_token = sys.argv[2]
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0"
root_folder = "."
delete_if_exist = True
ignore_clone_errors = True

gl = gitlab.Gitlab(gitlab_host, private_token=gitlab_token, user_agent=user_agent)


def clone_project(project):
    """Clone the repo keeping the folder structure."""
    ssh_url = project.ssh_url_to_repo
    folder = project.path_with_namespace

    path = os.path.join(root_folder, *folder.split("/"))
    if os.path.exists(path) and delete_if_exist:
        print("[*] deleting already present dir {}".format(path))
        shutil.rmtree(path)

    try:
        res = subprocess.run(
            ["git", "clone", ssh_url, path],
            check=True,
            stdout=subprocess.PIPE,
        )
    except Exception as e:
        if not ignore_clone_errors:
            raise
        print("[!] error cloning {}: {}".format(folder, str(e)))


def download_all():
    """Download all projects."""
    projects = gl.projects.list(iterator=True)
    for project in projects:
        print("[*] cloning project: {}...".format(project.name))
        clone_project(project)
    print("[+] done cloning all projects.")


if __name__ == "__main__":
    download_all()
