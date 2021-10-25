# syntax=docker/dockerfile:1

FROM python:3.9.5-slim
WORKDIR /home

COPY poetry.lock poetry.lock

RUN "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -"

RUN ["poetry", "install", "--no-dev"]

COPY . .

WORKDIR /home/source

ENTRYPOINT ["python", "bot.py"]
