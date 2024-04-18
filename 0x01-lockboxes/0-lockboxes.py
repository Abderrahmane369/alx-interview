#!/usr/bin/python3
'''ERRNO'''


def canUnlockAll(boxes):
    '''BOXK'''
    for k in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if k in boxes[box] and box != k:
                flag = True
                break
        
        if not flag:
            return False
    
    return True