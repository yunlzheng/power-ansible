# coding=utf-8
# !/usr/bin/python

from gittle import Gittle, GittleAuth

from power.config import ANSIBLE_ROLES


class Git():

    def clone(self, name, repo_url, key_file=None):
        auth = None
        if key_file:
            auth = GittleAuth(pkey=key_file)
        Gittle.clone(repo_url, "{0}/{1}".format(ANSIBLE_ROLES, name), auth=auth)

    def update(self, name, repo_url, key_file=None):
        auth = None
        if key_file:
            auth = GittleAuth(pkey=key_file)
        repo = Gittle("{0}/{1}".format(ANSIBLE_ROLES, name), auth=auth)
        repo.pull()


if __name__ == "__main__":
    git = Git()
    git.clone("ansible-role-apache", "https://github.com/geerlingguy/ansible-role-apache")