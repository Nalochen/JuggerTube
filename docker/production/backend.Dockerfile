FROM python:3.13-alpine

RUN apk add --no-cache  \
    g++ \
    linux-headers

WORKDIR /app

COPY ../../backend .

RUN pip install --no-cache-dir -r requirements.txt

COPY docker/production/provisioning /opt/scripts

RUN find /opt/scripts -type f -name "*" -exec chmod +x {} \;

ENV PYTHONPATH=/app
ENV SSL_CERT_PATH=/etc/letsencrypt/live/juggertube.de/fullchain.pem
ENV SSL_KEY_PATH=/etc/letsencrypt/live/juggertube.de/privkey.pem

EXPOSE 8080

CMD ["/opt/scripts/entrypoint.sh"]
