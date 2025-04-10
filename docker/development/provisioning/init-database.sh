#!/bin/sh

cd /app

. venv/bin/activate

python - <<END

from config.app import createApp
from DataDomain.Database.db import initDatabase

app = createApp()

initDatabase(app)

END
