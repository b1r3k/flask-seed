'''
 * Author: Lukasz Jachym
 * Date: 6/13/13
 * Time: 3:52 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''

import os

from flask import Flask
from logbook import Logger

import config
import blueprints
import routes
import utils

log = Logger(__name__)

def create_app(config_object):
    app = Flask(__name__, static_url_path='/static', static_folder='../static')
    app.register_blueprint(blueprints.restapi.blueprint, url_prefix='/api')

    app.config.from_object(config_object)

    override_env_name = 'FLASK_SEED_CONFIG'
    if app.config.from_envvar(override_env_name, silent=True):
        path = os.environ[override_env_name]
        log.info('Overriding config by environment variable: %s = %s' % (override_env_name, path))

    routes.create_routing(app)

    return app

### MAIN

config_name = os.getenv('CONFIG', 'Default')
app = create_app(config_object=config.defined[config_name])

if app.config['LOG_LEVEL'] == 'INFO':
    log_setup = utils.LoggingSetup(app.config['LOG_LEVEL'])
else:
    log_setup = utils.ProdLoggingSetup(app.config['LOG_LEVEL'], app.config['LOG_DIR'] + '%s.log' % app.config['APP_NAME'])


nested_log_setup = log_setup.get_default_setup()

with nested_log_setup.applicationbound():

    log.debug('Starting application...')

    if __name__ == '__main__':
        app.debug = True
        app.run()
