#!/usr/bin/python3
def canUnlockAll(boxes):
    '''Method that validate if all boxes were opened
       Use set for save opened boxes, unique values
       Iterate over keys array, and add new keys to opened set
       Retur True if all boxes opened, else False 
    '''
    opened = {0}
    keys = boxes[0]
    for key in keys:
        if key not in opened:
          keys += boxes[key]
          opened.add(key)
    return len(boxes) == len(opened)
