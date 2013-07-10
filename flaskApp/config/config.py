'''
 * Author: ca77y
 * Date: 7/07/13
 * Time: 19:55 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''

class Default(object):
    APP_NAME = 'flask-seed'
    DEBUG = False
    SECRET_KEY = '\x1e\xfa\xbe1\xf2\xc49\xd6\xb4c\xf1\xb4\t\x9cb\xcf.Og{\x1e\n@\xf7'
    LOG_LEVEL = 'WARNING'
    LOG_DIR = 'logs/'


class Dev(Default):
    DEBUG = True
    LOG_LEVEL = 'INFO'
