#!/usr/bin/python3
'''Implement task for Lockboxes project'''


def canUnlockAll(boxes):
    '''Method that validate if all boxes were opened
       Use set for save opened boxes, unique values
       Iterate over keys array, and, add new keys to opened set
       Return True if all boxes opened, else False
    '''

    opened = set([0])
    keys = boxes[0]
    for x in range(len(boxes)):
        if len(boxes[x]) == 0:
            opened.add(x)

    for key in keys:
        if key not in opened and key < len(boxes):
            keys += boxes[key]
            opened.add(key)
    return len(boxes) == len(opened)
