#!<YOUR_VIRTUALENV_PATH>/bin/python

from flup.server.fcgi import WSGIServer
from flaskApp.main import app as application

WSGIServer(application).run()
