# coding=utf-8
# !/usr/bin/python

class Task():

    def __init__(self, module_name="shell", module_params=None):
        self.module_name = module_name
        self.module_params = module_params