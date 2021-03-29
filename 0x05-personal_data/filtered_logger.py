#!/usr/bin/env python3
'''
This module contains the function filter_datum
'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Returns a log message, obfuscated
    '''
    for field in fields:
        message = re.sub(f'(?<={field}=)[^{separator}]*', redaction, message)
    return message
