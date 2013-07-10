'''
 * Author: Lukasz Jachym
 * Date: 7/10/13
 * Time: 4:41 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''
import inspect

import config

from config import *

config_list = inspect.getmembers(config, inspect.isclass)
defined = dict(config_list)