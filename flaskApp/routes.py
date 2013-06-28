'''
 * Author: Lukasz Jachym
 * Date: 6/13/13
 * Time: 3:57 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''

from flask import render_template
from flask.views import View


class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)


views = [{'endpoint': '/', 'view_func': RenderTemplateView.as_view('index', template_name='index.jinja2')},
]

def create_routing(app):
    for view in views:
        app.add_url_rule(view['endpoint'], view_func=view['view_func'])
