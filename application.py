# -*- coding: utf-8 -*-

import os

import logging
from log_handler import MakeFileHandler

from flask import Flask, Response
import json

app = Flask(__name__)

handler = MakeFileHandler('application.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('werkzeug')
logger.addHandler(handler)

@app.route("/<resource>", methods=['GET'])
def echo(resource):
  return Response(response=json.dumps({ "echo": resource}) ,status=200, mimetype='application/json')

if __name__ == "__main__":
  app.run(host="0.0.0.0")
