#!/usr/bin/python3
"""
UTF-8 validation function
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    bits_count = 0
    for num in data:
        if bits_count == 0:
            mask = 1 << 7
            while (num & mask) != 0:
                bits_count += 1
                mask >>= 1
            if bits_count == 1 or bits_count > 4 or (num & 128) != 0:
                return False
            continue
        if not (num & 192 == 128):
            return False
        bits_count -= 1

    return bits_count == 0
