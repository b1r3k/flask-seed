'''
 * Author: Lukasz Jachym
 * Date: 6/28/13
 * Time: 3:49 PM
 *
 * This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.
'''

import logbook

def get_logging_setup(log_level, log_filename):
    format_string = '{record.channel}: {record.message}'

    time_rotating_handler = logbook.TimedRotatingFileHandler(log_filename,
                                                         date_format='%Y-%m-%d',
                                                         format_string=format_string)

    stderr_handler = logbook.StderrHandler(level=log_level)
    stderr_handler.format_string = format_string
    stderr_handler.formatter

    nested_log_setup = logbook.NestedSetup([ stderr_handler, time_rotating_handler ])

    return nested_log_setup