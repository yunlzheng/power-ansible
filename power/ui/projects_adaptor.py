# coding=utf-8
# !/usr/bin/python
from flask import render_template
from power.ui.request_adaptor import RequestAdaptor


class ProjectsAdaptor(RequestAdaptor):

    def __init__(self, request, uuid=None):
        self.uuid = uuid
        RequestAdaptor.__init__(self, request)

    def get(self, *args, **kwargs):
        return render_template('admin/projects.html')