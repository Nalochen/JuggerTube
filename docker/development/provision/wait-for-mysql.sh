#!/bin/sh

if ! nc -z mysql 3306; then
  echo "Waiting for MySQL to start"
  while ! nc -z mysql 3306; do
    sleep 1
  done
  echo "MySQL started"
fi

exec "$@"
