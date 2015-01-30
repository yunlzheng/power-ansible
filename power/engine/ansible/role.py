# coding=utf-8
#!/usr/bin/python

import yaml
import os

class Role(object):

    def __init__(self, name=None, abs_path=None):
        self.name = name
        self.meta = None
        if "meta" in os.listdir(abs_path):
            with file(os.path.sep.join([abs_path, "meta", "main.yml"])) as meta:
                meta = Meta.load_from_yaml(yaml.load(meta))
                self.meta=meta

    def __str__(self):
        return self.name+"{" + self.meta.__str__() +"}"

class Meta():

    def __init__(self, meta):
        self.description = meta['galaxy_info'].get('description', "")
        self.license = meta['galaxy_info'].get('license', "")
        self.author = meta['galaxy_info'].get('author', "")
        self.company = meta['galaxy_info'].get('company', "")
        self.platforms = meta['galaxy_info'].get('platforms', [])
        self.dependencies = meta['galaxy_info'].get('dependencies', [])
        self.categories = meta['galaxy_info'].get('categories', [])
        self.min_ansible_version= meta['galaxy_info'].get('min_ansible_version', "")

    def __str__(self):
        return "-".join([self.description, self.license])

    @classmethod
    def load_from_yaml(cls, yaml):
        return cls(yaml)

class Platform():

    support_platforms = ['Ubuntu', 'Centos']

    def __init__(self):
        self.name=""
        self.versions=""

if __name__ == "__main__":
    role = Role(name="simple role", abs_path="/vagrant/examples/simple-roles")
    print role