#usr/bin/env python3

""" first locking boxes"""
def canUnlockAll(boxes):

    final = [0]
    for i, box in enumerate(boxes):
        for key in box:
            if key not in final and key!=i :
                final.append(key)
    return len(final) == len(boxes)            
