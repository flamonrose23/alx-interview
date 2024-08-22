#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Method determines if given data set representing
    valid UTF-8 encoding
    """
    number_bytes = 0
    for number in data:
        binary_rep = format(number, '#010b')[-8:]
        if number_bytes == 0:
            for bit in binary_rep:
                if bit == '0':
                    break
                number_bytes += 1
            if number_bytes == 0:
                continue
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            if not (binary_rep[0] == '1' and binary_rep[1] == '0'):
                return False
        number_bytes -= 1
    return number_bytes == 0
