#Flask Dependencies
from flask import Flask, Blueprint, request, render_template
#System Dependencies

#Module Configuration
from repost.core.functions import *
mod_core = Blueprint('core', __name__, url_prefix='/')

@mod_core.route('/mail')
def mailer():
    pass

