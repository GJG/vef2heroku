
from sys import argv

import bottle *
#from bottle import *

bottle.debug(True)

@get('/')
def index():
    return "<h1>Halló heimur á Heroku hýsingu og Github geymslu</h1>"

run(host='0.0.0.0', port=argv[1])

# if os.environ.get('APP_LOCATION') == 'heroku':	 
#    bottle.run(host='0.0.0.0', port=argv[1])
# else:
#    run(host='localhost', port=8080, debug=True)