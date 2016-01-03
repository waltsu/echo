from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "log"
class MakeFileHandler(RotatingFileHandler):
  def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=0):
    try:
      os.makedirs(LOG_DIR)
    except OSError:
      if os.path.isdir(LOG_DIR):
          pass
      else: raise
    RotatingFileHandler.__init__(self, "%s/%s" % (LOG_DIR, filename), mode=mode, maxBytes=maxBytes, backupCount=backupCount, encoding=encoding, delay=delay)
