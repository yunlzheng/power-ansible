FROM ubuntu:14.04
MAINTAINER Yunlong Zheng yunl.zheng@gmail.com
ENV REFRESHED_AT 2015-2-7

RUN apt-get update
RUN apt-get install python-pip

ADD . /vagrant
WORKDIR /vagrant

RUN pip install -r requirements.txt
EXPOSE 5001
