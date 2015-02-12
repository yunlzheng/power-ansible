# coding=utf-8
# !/usr/bin/python
import os
import yaml
from setting import ANSIBLE_PLAYBOOKS
from playbook import Playbook
from fabric.api import lcd, local


class Ansible():

    def __init__(self, id, hosts=None, playbooks=None):
        self.id = id
        self.hosts = hosts
        self.playbooks = playbooks
        self.data = []

    def generate(self, work_dir):
        for playbook in self.playbooks:
            self.data.append(playbook.__dict__)
        with file(work_dir+"/playbook.yml", "w") as f:
            yaml.dump(self.data, f)

    def run(self):
        '''
        Generate ansible playbook and run
        :return: None
        '''
        if not os.path.exists(ANSIBLE_PLAYBOOKS):
            os.mkdir(ANSIBLE_PLAYBOOKS)

        work_dir = ANSIBLE_PLAYBOOKS + "/" + self.id
        if not os.path.exists(work_dir):
            os.mkdir(work_dir)
        self.generate(work_dir)
        with lcd(work_dir):
            local("ansible-playbook -i hosts playbook.yml")

if __name__ == "__main__":
    playbook01 = Playbook(hosts="all", sudo=True, gather_facts=True)
    playbook02 = Playbook(hosts="all", sudo=True, gather_facts=True, roles=['ansible-role-apache'])
    ansible = Ansible("10", playbooks=[playbook01, playbook02])
    ansible.run()
