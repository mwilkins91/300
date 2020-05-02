FROM node:12.16.3-alpine3.10

RUN apk add --update-cache \
  python3 \
  build-base \
  && pip3 install pipenv \
  && rm -rf /var/cache/apk/*

WORKDIR /app

COPY . ./
RUN pipenv install
RUN npm install

EXPOSE 3000
CMD ["pipenv", "run", "node", "server.js"]
