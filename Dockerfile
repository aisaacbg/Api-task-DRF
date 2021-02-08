FROM python:3.8
#log
ENV PYTHONUMBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install -r requirements.txt 

COPY . /code/