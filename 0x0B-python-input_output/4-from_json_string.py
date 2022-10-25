#!/usr/bin/python3
"""
converts to str from json
"""

import json


def from_json_string(my_str):
    """converts to str from json"""
    return json.loads(my_str)
