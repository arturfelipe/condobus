FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y binutils libproj-dev gdal-bin postgresql-client

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN make setup
