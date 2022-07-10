#Import flask and template operators
from flask import Flask, render_template

#Define WSGI Application
app = Flask(__name__)
app.config.from_pyfile('flask_config.py')

#Enable Cross Origin
#If we have other webservers that want to hit our api, we need to whitelist them here (or be lazy and accept any incoming connection)
#from flask_cors import CORS
#cors_rt = CORS(app, resources={r"/api/*": {"origins": "*"}})

#Import Developer Defined Modules
from repost.core.controller import mod_core
from repost.api.controller import *

#Register Blueprints
app.register_blueprint(mod_core)
#app.register_blueprint(api_module)

#Site-wide error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

#Site Root
@app.route('/')
def index():
    return render_template('base.html')

