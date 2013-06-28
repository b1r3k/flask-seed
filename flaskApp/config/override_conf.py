'''
 * Author: Lukasz Jachym
 * Date: 6/28/13
 * Time: 1:19 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''

import os

def override_by_env(cfg_globals):

    cfg_vars = filter(lambda obj: obj.isupper(), cfg_globals.keys())

    for cfg_symbol in cfg_vars:
        os.environ.get(cfg_symbol)