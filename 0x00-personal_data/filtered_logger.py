#!/usr/bin/env python3
""" Regex-ing and Obfuscating info """
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscates certain field values in a log message."""
    pattern = (
            f'({re.escape(fields[0])}={re.escape(separator)}[^{re.escape(separator)}]+|'
            f'{re.escape(fields[1])}={re.escape(separator)}[^{re.escape(separator)}]+)'
            )
    replacement = f'{fields[0]}={redaction}{separator}{fields[1]}={redaction}{separator}'
    return re.sub(pattern, replacement, message)
