FROM python:3.8.12-slim-buster
LABEL org.opencontainers.image.source='https://github.com/BRG-code/our-discord-server-bot'
COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "main.py"]