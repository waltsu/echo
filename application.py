# -*- coding: utf-8 -*-

from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/<resource>", methods=['GET'])
def echo(resource):
  return Response(response=json.dumps({ "echo": resource}) ,status=200, mimetype='application/json')

if __name__ == "__main__":
  app.run(host="0.0.0.0")
