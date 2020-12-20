FROM node:15.4.0-alpine3.10

RUN sed -i -e 's/v[[:digit:]]\..*\//edge\//g' /etc/apk/repositories
RUN apk add --update python2 libexecinfo-dev build-base libtool autoconf automake
ENV PYTHON /usr/bin/python2

# Build project
RUN mkdir -p /opt/cyber-punks/website
WORKDIR /opt/cyber-punks/website

COPY package.json yarn.lock ./
RUN yarn install

COPY public/ public/
COPY src/ src/

RUN yarn build

# Serve project
ENTRYPOINT yarn serve
