FROM ubuntu

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y python3 python3-pip 

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential 

COPY requirements.txt /

RUN pip install --upgrade pip &&\
    pip install -r /requirements.txt

WORKDIR /tmp
RUN django-admin.py startproject admin

