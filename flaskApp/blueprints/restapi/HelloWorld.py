'''
 * Author: Lukasz Jachym
 * Date: 6/27/13
 * Time: 5:58 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''
from functools import wraps

from flask import Response, request
from flask.ext import restful

def check_auth(auth):

    if not auth:
        return False

    return False

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if check_auth(request.authorization):
            return func(*args, **kwargs)

        return Response('Could not verify your access level for that URL.\n'
                        'You have to login with proper credentials', 401,
                        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return wrapper

class ProtectedResource(restful.Resource):
    method_decorators = [authenticate]

class HelloWorld(restful.Resource):

    def get(self):
        return {'msg': 'hello world!'}

class SecretWorld(ProtectedResource):

    def get(self):
        return {'msg': 'hello secret world!'}