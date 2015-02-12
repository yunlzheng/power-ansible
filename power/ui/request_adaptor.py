# coding=utf-8
# !/usr/bin/python


class RequestAdaptor():

    def __init__(self, request):
        self.request = request

    def handle(self, *args):
        method = getattr(self, self.request.method.lower())
        return method()

    def get(self, *args, **kwargs):
        raise Exception("unsupported method")

    def delete(self, *args, **kwargs):
        raise Exception("unsupported method")

    def put(self, *args, **kwargs):
        raise Exception("unsupported method")

    def post(self, *args, **kwargs):
        raise Exception("unsupported method")


if __name__ == "__main__":
    request = {"method": "get"}
    request_adaptor = RequestAdaptor(request)
    request_adaptor.handle()
