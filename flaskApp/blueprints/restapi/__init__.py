'''
 * Author: Lukasz Jachym
 * Date: 6/17/13
 * Time: 6:01 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''

from flask import Blueprint, render_template, abort
from flask.ext.restful import Api
from jinja2 import TemplateNotFound

import HelloWorld

def create_routing(blueprint):
    blueprint.add_resource(HelloWorld.HelloWorld, '/hello')
    blueprint.add_resource(HelloWorld.SecretWorld, '/secret')

blueprint = Blueprint('restful', __name__, template_folder='templates')

# dirty hack due to: https://github.com/twilio/flask-restful/issues/97
blueprint.handle_exception = None
blueprint.handle_user_exception = None

api = Api(blueprint, catch_all_404s=True)

create_routing(api)
