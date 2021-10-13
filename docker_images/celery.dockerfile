FROM python:3.8

RUN pip install celery==5.1.2 redis==3.5.3

RUN pip install gevent eventlet
WORKDIR /src
