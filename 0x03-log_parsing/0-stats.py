#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import re
import sys


count = 0
size = 0
status = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}


def print_statistics():
    print(f"File size: {size}")
    for key, value in status.items():
        if value:
            print(f'{key}: {value}')


try:
    while True:
        line = sys.stdin.readline()
        line_parts = line.split()
        count += 1
        try:
            size += int(line_parts[-1])
            if line_parts[-2] in status:
                status[line_parts[-2]] += 1
        except (IndexError, ValueError):
            pass
        if not line:
            print_statistics()
            break
        if count == 10:
            print_statistics()
            count = 0
except KeyboardInterrupt:
    print_statistics()
    raise