#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import *

bottle.debug(True)

@get('/')
def index():
    return "<h1>Halló heimur á Heroku hýsingu og Github geymslu</h1>"

bottle.run(host='0.0.0.0', port=argv[1])

# if os.environ.get('APP_LOCATION') == 'heroku':	 
#    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
# else:
#    run(host='localhost', port=8080, debug=True)