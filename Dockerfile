FROM ubuntu:14.04
MAINTAINER Yunlong Zheng yunl.zheng@gmail.com
ENV REFRESHED_AT 2015-2-7

ADD ./provision/roles/common/files/sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install python-pip python-dev -y

ADD . /vagrant
WORKDIR /vagrant

RUN pip install -r requirements.txt -i http://pypi.douban.com/simple
EXPOSE 5001

CMD ['python server.py']