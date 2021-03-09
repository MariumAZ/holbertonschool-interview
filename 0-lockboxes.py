#usr/bin/env python3

""" first locking boxes"""
def canUnlockAll(boxes):
      """Determines if all the boxes can be opened or not
    Args:
        boxes (list[list]): boxes is the list of box that contains keys
    Returns:
        (bool): True if we can open all the boxes, otherwise return False
    """
    final = [0]
    for i, box in enumerate(boxes):
        for key in box:
            if key not in final and key!=i :
                final.append(key)
    return len(final) == len(boxes)            
