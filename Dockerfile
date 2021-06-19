# syntax=docker/dockerfile:1

FROM python:3.9.5-slim
WORKDIR /home

COPY . .

RUN ["pip", "install", "--no-cache", "-r", "requirements.txt"]
WORKDIR /home/source

ENTRYPOINT ["python", "bot.py"]
