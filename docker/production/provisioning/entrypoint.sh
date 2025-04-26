#!/bin/sh

if ! nc -z mysql 3306; then
  echo "Waiting for MySQL to start"
  timeout=30
  while ! nc -z mysql 3306; do
    sleep 1
    timeout=$((timeout-1));
    if [ $timeout -le 0 ]; then
      echo "Timeout waiting for MySQL"
      exit 1
    fi
  done
  echo "MySQL started"
fi

/usr/local/bin/init-database.sh

exec gunicorn \
  --certfile="${SSL_CERT_PATH}" \
  --keyfile="${SSL_KEY_PATH}" \
  -w 5 \
  -b 0.0.0.0:8080 wsgi:app
