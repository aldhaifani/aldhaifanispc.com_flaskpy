import os
import sys

from public import create_app


sys.path.insert(0, os.path.dirname(__file__))


def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])

    application = create_app

    return [application]
