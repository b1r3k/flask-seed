'''
 * Author: Lukasz Jachym
 * Date: 6/27/13
 * Time: 4:54 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''

from settings import *

from override_conf import override_by_env

override_by_env(globals())