#!/usr/bin/python3
"""
    Function that checks if a box contains a key that can open other boxes.
"""


def canUnlockAll(boxes):
    """
        checks boxes to see if they contain keys to open each other
    """
    if not boxes or not boxes[0]:
        return False

    number_of_keys = [0]
    number_of_boxes = len(boxes)

    for keys in number_of_keys:
        for box in boxes[keys]:
            if box < number_of_boxes and box not in number_of_keys:
                number_of_keys.append(box)

    return len(number_of_keys) == number_of_boxes
