#usr/bin/env python3

def canUnlockAll(boxes):


    if boxes[0] == [] or not isinstance(boxes,list):
        return False
    final = [0]
    for i, box in enumerate(boxes):
        for key in box:
            if key not in final and key!=i :
                final.append(key)
    return len(final) == len(boxes)            
