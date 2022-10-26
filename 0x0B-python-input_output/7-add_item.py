#!/usr/bin/python3
"""
scipt to add args to a jsoonfile
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except Exception:
    json_list = []

for ar in argv[1:]:
    json_list.append(ar)

save_to_json_file(json_list, filename)
