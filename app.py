from sys import argv

import bottle
from bottle import *
bottle.debug(True)

 
@route("/")
def index():
    return """
    <h2>Verkefnki 1</h1>
    <a href="/about">About</a>
    <a href="/bio">Bio</a>
    <a href="/pic">Pictures</a>
"""

@route("/about")
def elvar():
    return "Hér er sögn um mig"

@route("/bio")
def elvar():
    return"Hér er Biograph"

@route("/pic")
def elvar():
    return "Hér er ljósmynd"


bottle.run(host='0.0.0.0', port=argv[1])



"""
from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    return "<h1>Halló heimur á Heroku hýsingu og Github geymslu</h1>"

bottle.run(host='0.0.0.0', port=argv[1])
"""
# run(host='localhost', port=8080, debug=True)
