#!/usr/bin/env python3
""" Regex-ing and Obfuscating info """
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
                """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super(RedactingFormatter, self).format(record)
        return self.filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)
    
    @staticmethod
    def filter_datum(fields, redaction, message, separator):
        """Obfuscates certain field values in a log message."""
        pattern = (
                f'({re.escape(fields[0])}={re.escape(separator)}[^{re.escape(separator)}]+|'
                f'{re.escape(fields[1])}={re.escape(separator)}[^{re.escape(separator)}]+)'
            )
        replacement = f'{fields[0]}={redaction}{separator}{fields[1]}={redaction}{separator}'
        return re.sub(pattern, replacement, message)
