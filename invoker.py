from werkzeug.exceptions import InternalServerError
import os
import shutil

from flask import Flask
from flask import request
from flask import abort
from subprocess import call

import invokeRender

app = Flask(__name__)

@app.route('/')
def invoke():
	return invokeRender.renderRequest(request)

@app.after_request
def cleanup(response):
    location = '/tmp/renders'
    if os.path.isdir(location):
        shutil.rmtree(location)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)