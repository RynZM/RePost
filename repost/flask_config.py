#Web Server Framework Configuration File
import os,sys

#Application Variable Defaults
PORT = ''
PREFIX = '/'
FORCE_SCRIPT_NAME = '/'
APPLICATION_ROOT = '/'

#Environment Dependent Variables
if 'gunicorn' in os.environ.get("SERVER_SOFTWARE", ""):
    PREFIX = '/apps/repost'
    FORCE_SCRIPT_NAME = '/apps/repost'
    APPLICATION_ROOT = '/apps/repost'
    DEPLOYED_APPLICATION_HOST = '--'
else:
    #pull dev port out of args
    for i in range(0, len(sys.argv)):
        if sys.argv[i] == '--port':
            PORT = sys.argv[i+1]
            break
    DEPLOYED_APPLICATION_HOST = f'http://127.0.0.1:{PORT}'

DEPLOYMENT_URI = DEPLOYED_APPLICATION_HOST + APPLICATION_ROOT

#Flask Variables
DEBUG = False
THREADS_PER_PAGE = 1
PROPOGATE_EXCEPTIONS = False
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#SSL/Browser Security
CSRF_ENABLED = True
CSRF_SESSION_KEY = "recookie"
SECRET_KEY = "recookie"


