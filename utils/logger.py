import coloredlogs
import logging
import os

from logging import handlers

FORMAT = "%(asctime)s|{}|%(levelname)s|%(message)s"

LOG_DIR = "logs"
LOG_FILE_NAME = "amazonbot.log"
if not os.path.exists(LOG_DIR):
    try:
        os.makedirs(LOG_DIR)
    except OSError:
        raise

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

if os.path.isfile(LOG_FILE_PATH):
    rollover_handler = handlers.RotatingFileHandler(
        LOG_FILE_PATH, backupCount=10, maxBytes=100 * 1024 * 1024
    )
    try:
        rollover_handler.doRollover()
    except Exception:
        pass

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format=FORMAT,
)

log = logging.getLogger("amazonbot")
log.setLevel(logging.DEBUG)

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(FORMAT))

log.addHandler(stream_handler)

coloredlogs.install(LOGLEVEL, logger=log, fmt=FORMAT)