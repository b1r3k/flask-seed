'''
 * Author: Lukasz Jachym
 * Date: 6/13/13
 * Time: 3:52 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''

from flask import Flask

import config
import blueprints
import routes

def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='../static')
    app.register_blueprint(blueprints.restapi.blueprint, url_prefix='/api')

    routes.create_routing(app)

    return app


app = create_app()

app.config.from_object(config)

if __name__ == '__main__':
    app.debug = True
    app.run()