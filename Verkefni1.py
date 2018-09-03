from sys import argv

import bottle
from bottle import *
bottle.debug(True)

@route("/")

def index():
    return """
    <h1>Verkefni 1</h1>
    <a href='/stuff'>stuff</a>
    <a href='/stuff1'>stuff1</a>
    <a href='/stuff2'>stuff2</a>
    """

@route("/stuff")
def stuff():
    return "<h2>Hérna er stuff</h2>"

@route("/stuff1")
def stuff():
    return "<h2>Hérna er meira stuff</h2>"

@route("/stuff2")
def stuff():
    return "<h2>Hérna er enn meira stuff</h2>"

bottle.run(host="0.0.0.0", port=argv[1])
