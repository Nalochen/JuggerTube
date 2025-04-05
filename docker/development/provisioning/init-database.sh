#!/bin/sh

cd /app

. venv/bin/activate

python - <<END

from config.app import createApp

app = createApp()

END
