FROM node:15.4.0-alpine3.10

# Build project
RUN mkdir -p /opt/cyber-punks/website
WORKDIR /opt/cyber-punks/website

COPY package.json yarn.lock .
RUN yarn install

COPY tsconfig.json .
COPY public/ public/
COPY src/ src/

RUN yarn build

# Serve project
ENTRYPOINT yarn start
