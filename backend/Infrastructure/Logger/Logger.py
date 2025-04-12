import logging
import os

from DataDomain.Database.db import db
from DataDomain.Model.LogHandler import LogHandler

logger = logging.getLogger('juggertube_mysql_logger')

lowestLogLevel = logging.DEBUG if os.getenv(
    'FLASK_ENV') == 'development' else logging.INFO
logger.setLevel(lowestLogLevel)


dbHandler = LogHandler(db.session)
formatter = logging.Formatter('%(message)s')
dbHandler.setFormatter(formatter)

logger.addHandler(dbHandler)
