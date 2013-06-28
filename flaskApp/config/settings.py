'''
 * Author: Lukasz Jachym
 * Date: 6/27/13
 * Time: 4:55 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''

### all settings should be defined as uppercase!
### overriden by env vars (via forman & .env file)
DEBUG = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
TESTING = False
DEBUG_TB_ENABLED = False
SECRET_KEY = '\x1e\xfa\xbe1\xf2\xc49\xd6\xb4c\xf1\xb4\t\x9cb\xcf.Og{\x1e\n@\xf7'
LOG_LEVEL = 'INFO'

MONGODB_URI = 'mongodb://PUT_YOUR_DB_HERE'
MONGODB_DBNAME = 'YOUR_DB_NAME'
