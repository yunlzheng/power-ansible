# coding=utf-8
# !/usr/bin/python


class Hosts():

    def __init__(self, hosts=None):
        self.hosts = {}

    def add_host(self, ip, remote_user, port, group_name=None, private_key=None):
        host = Host(ip, remote_user, port)
        if not self.hosts.has_key(group_name):
            self.hosts[group_name] = []
        self.hosts[group_name].append(host)


class Host():

    def __init__(self, ip, remote_user, port):
        self.ip = ip
        self.remote_user = remote_user
        self.port = port

if __name__ == "__main__":
    hosts = Hosts()
    hosts.add_host("127.0.0.1", "vagrant", "2222", "vagrant_groups")
    hosts.add_host("127.0.0.1", "vagrant", "2211", "vagrant_groups")
    hosts.add_host("127.0.0.1", "vagrant", "2223", "vagrant_groups2")
    print hosts.__dict__
    #print json.dumps(hosts)