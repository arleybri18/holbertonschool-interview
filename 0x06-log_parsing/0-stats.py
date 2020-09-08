#!/usr/bin/python3
""" 0. Log parsing
Write a script that reads stdin line by line and computes metrics
"""
import sys
import signal

line_count = 1
file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}


def print_values():
    """ Print formated values"""

    print("File size: {:d}".format(file_size))
    for k, v in status_codes.items():
        if v > 0:
            print("{:s}: {:d}".format(k, v))


def reset_values():
    """ Clean values """

    global line_count, file_size, status_codes
    line_count = 1
    file_size = 0
    for k in status_codes.keys():
        status_codes[k] = 0


def signal_handler(sig, frame):
    """signal_handler"""

    print_values()


def read_stdin():
    """ Read stdin lines """

    global line_count, file_size, status_codes
    for line in sys.stdin:
        if line != "":
            aux = line.rstrip().split('"')
            aux = aux[2].split()
            status_codes[aux[0]] += 1
            file_size += int(aux[1])
            line_count += 1
            if line_count > 10:
                print_values()
                reset_values()
            signal.signal(signal.SIGINT, signal_handler)


read_stdin()
print_values()
