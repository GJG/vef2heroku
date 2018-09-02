#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    return "Halló heimur á Heroku hýsingu og Github geymslu"



if os.environ.get('APP_LOCATION') == 'heroku':
	bottle.run(host='0.0.0.0', port=argv[1])
#    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)