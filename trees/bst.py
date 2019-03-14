#!/usr/bin/env

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sortedArrayToBST(a):
    if not a:
        return None
    middle = int(len(a) / 2)
    print('middle = %s' % middle)
    root = Node(a[middle])
    root.left = sortedArrayToBST(a[:middle])
    root.right = sortedArrayToBST(a[middle + 1:])
    return root
