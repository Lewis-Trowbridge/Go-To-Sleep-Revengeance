# syntax=docker/dockerfile:1

FROM python:3.9.5-slim
WORKDIR /home

RUN [ "pip", "install", "--no-cache", "poetry" ]

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN ["poetry", "install", "--no-dev"]

COPY . .

WORKDIR /home/source

ENTRYPOINT ["poetry", "run", "python", "bot.py"]
