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

where_are_we_path = os.path.dirname(os.path.dirname(__file__))


def create_app(config_object=config.Default):
    app = Flask(__name__, static_url_path='/static', static_folder='../static')
    app.register_blueprint(blueprints.restapi.blueprint, url_prefix='/api')

    app.config.from_object(config_object)
    app.config.from_envvar('FLASK_SEED_CONFIG', silent=True)

    routes.create_routing(app)

    return app


app = create_app()
logger = utils.get_logging_setup(app.config['LOG_LEVEL'], where_are_we_path + '/logs/%s.log' % __name__)

with logger.applicationbound():
    log = Logger(__name__)
    log.debug('Starting application...')

    if __name__ == '__main__':
        app.debug = True
        app.run()