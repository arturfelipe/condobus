FROM node:latest

RUN mkdir /code
WORKDIR /code

COPY package.json /code/
COPY yarn.lock /code/

COPY src /code/src
COPY public /code/public

RUN yarn install
