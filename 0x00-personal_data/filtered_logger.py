#!/usr/bin/env python3
""" Returns the log message obfuscated """

import re
import logging


def filter_datum(fields, redaction, message, separator):
    """ function uses a regex to replace occurrences of certain field values
        Args:
            fields: a list of strings representing all fields to obfuscate
            redaction: string representing by what the field will be obfuscated
            message: a string representing the log line
            separator: string representing by which character is separating
    """
    return re.sub(f'({re.escape(fields[0])}={re.escape(separator)}[^{re.escape(separator)}]+|'
            f'{re.escape(fields[1])}={re.escape(separator)}[^{re.escape(separator)}]+)', 
            f'{fields[0]}={redaction}{separator}{fields[1]}={redaction}{separator}', message)
