FROM python:3.13-slim

RUN apt-get update && apt-get install -y cron procps

WORKDIR /app

COPY ../../backend/pyproject.toml .

RUN python -m pip install .

COPY scripts /app/scripts
COPY docker/production/crontab.txt /app/crontab.txt

RUN crontab /app/crontab.txt

CMD cron -f
