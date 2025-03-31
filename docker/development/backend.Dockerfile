FROM python:3.13-alpine

WORKDIR /app

COPY ../../backend .

RUN mkdir /opt/scripts

COPY docker/development/provisioning /opt/scripts
COPY docker/development/scripts /usr/local/bin

RUN find /opt/scripts -type f -name "*" -exec chmod +x {} \;
RUN find /usr/local/bin -type f -name "*" -exec chmod +x {} \;

ENV PYTHONPATH=/app

EXPOSE 8080

CMD ["/opt/scripts/entrypoint.sh"]
