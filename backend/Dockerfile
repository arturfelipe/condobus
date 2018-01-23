FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y binutils libproj-dev gdal-bin postgresql-client

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r requirements-test.txt
