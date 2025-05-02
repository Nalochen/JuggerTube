FROM python:3.13-alpine

WORKDIR /app

COPY ../../backend/pyproject.toml .

RUN python -m pip install .

COPY ../../backend .

COPY docker/production/provisioning /usr/local/bin

RUN find /usr/local/bin -type f -name "*" -exec chmod +x {} \;

VOLUME ["/etc/letsencrypt"]

ENV PYTHONPATH=/app
ENV SSL_CERT_PATH=/etc/letsencrypt/live/juggertube.de/fullchain.pem
ENV SSL_KEY_PATH=/etc/letsencrypt/live/juggertube.de/privkey.pem

EXPOSE 8080

ENTRYPOINT ["entrypoint.sh"]
