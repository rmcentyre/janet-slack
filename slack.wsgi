import sys

path = '/var/www/slack.rmcentyre.com/public'
if path not in sys.path:
    sys.path.append(path)
 
from slack import app as application
