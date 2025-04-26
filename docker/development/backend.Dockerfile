FROM python:3.13-alpine

WORKDIR /app

COPY ../../backend/pyproject.toml .

RUN python -m pip install .

COPY ../../backend .

RUN mkdir /opt/scripts

COPY docker/development/provision /usr/local/bin
COPY docker/development/scripts /usr/local/bin

RUN find /usr/local/bin -type f -name "*" -exec chmod +x {} \;

ENV PYTHONPATH=/app

EXPOSE 8080

ENTRYPOINT ["wait-for-mysql.sh"]

CMD ["python", "run.py"]
