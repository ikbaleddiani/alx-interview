#!/usr/bin/python3
"""Unlock list of lists"""

def canUnlockAll(boxes):
    """This function will take a list of lists where the content
    of each list represents keys to unlock other lists"""

    keys = [0]
    for key in keys:
        for box_key in boxes[key]:
            if box_key not in keys and box_key < len(boxes):
                keys.append(box_key)
    return len(keys) == len(boxes)