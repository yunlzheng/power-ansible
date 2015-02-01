# coding=utf-8
# !/usr/bin/python

from __future__ import with_statement

import paramiko


class SSH():

    def __init__(self, host, username, password, port=22):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.transport = None

    def authorized_local(self):
        src = "~/.ssh/id_rsa.pub"
        des = "/home/{0}/.ssh/authorized_keys".format(self.username)
        if (self.exists(des)):
            pass
            # sftp = self.get_sftp_client()
            # with sftp.open(des) as authorized_keys:
            #     authorized_keys.write()
        self.put(src, des)

    def exists(self, path):
        sftp = self.get_sftp_client()
        try:
            sftp.lstat(path)
        except IOError:
            return False
        finally:
            self.close()
        return True

    def put(self, local_path, remote_path):
        sftp = self.get_sftp_client()
        sftp.put(local_path, remote_path)
        self.close()

    def get_sftp_client(self):
        if self.transport is None:
            self.transport = paramiko.Transport((self.host, self.port))
            self.transport.connect(username=self.username, password=self.password)
        return paramiko.SFTPClient.from_transport(self.transport)

    def close(self):
        if self.transport is not None:
            self.transport.close()

