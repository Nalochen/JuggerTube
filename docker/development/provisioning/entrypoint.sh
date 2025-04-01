#!/bin/sh

if [ ! -d "venv" ]; then
  echo "Erstelle virtuelle Umgebung..."
  python3 -m venv venv
fi

. venv/bin/activate
pip install -r requirements.txt

if [ ! nc mysql 3306 ]; then
  echo "Waiting for MySQL to start"
  while ! nc -z mysql 3306; do
    sleep 1
  done
  echo "MySQL started"
fi

/opt/scripts/init-database.sh

python3 run.py
