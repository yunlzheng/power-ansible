# coding=utf-8
# !/usr/bin/python
from hosts import Hosts


class Playbook():

    def __init__(self, hosts=None, sudo=False, gather_facts=False, tasks=None, roles=None, vars=None, vars_files=None):
        self.hosts = hosts
        self.gather_facts = gather_facts
        self.sudo = sudo
        self.tasks = tasks
        self.roles = roles

if __name__ == "__main__":

    hosts = Hosts()
    hosts.add_host("127.0.0.1", "vagrant", "2222", "vagrant_groups")
    playbook = Playbook(hosts="vagrant_groups")
    print playbook.__dict__