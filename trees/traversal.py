#!/usr/bin/env python3

"""

Binary tree example:

        1
       / \
      2   3
     /     \
    4       5
           / \
          6   7

"""

from bst import sortedArrayToBST

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printAllNodes(node):
    print(node.data)
    if node.left is None and node.right is None:
        return
    if node.left is not None:
        printAllNodes(node.left)
    if node.right is not None:
        printAllNodes(node.right)

def getTreeHeight(root):
    if root is None:
        return 0
    lheight = getTreeHeight(root.left)
    rheight = getTreeHeight(root.right)

    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print ('%s' % root.data)
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level -1)

def getGivenLevel(root, level):
    if root is None:
        return []
    if level == 1:
        return [root.data]
    elif level > 1:
        return getGivenLevel(root.left, level - 1) + \
               getGivenLevel(root.right, level - 1)

def getLeftView(root):
    result = []
    for level in range(1, getTreeHeight(root) + 1):
        result.append(getGivenLevel(root, level)[0])
    return result

def getRightView(root):
    result = []
    for level in range(1, getTreeHeight(root) + 1):
        result.append(getGivenLevel(root, level)[-1])
    return result

def printLevelOrder(root):
    for level in range(1, getTreeHeight(root) + 1):
        printGivenLevel(root, level)

# Inorder tree traversal

def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)

def printPreorder(root):
    if root is not None:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root is not None:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.right.right = Node(5)
n1.right.right.left = Node(6)
n1.right.right.right = Node(7)
"""
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
"""
print('Height = %s' % getTreeHeight(n1))
printGivenLevel(n1, 3)
printLevelOrder(n1)
print('Level 3:')
print(getGivenLevel(n1, 2))
print('Left view:')
print(getLeftView(n1))
print('Right view:')
print(getRightView(n1))

print('Inorder traversal')
printInorder(n1)
print('Preorder traversal')
printPreorder(n1)
print('Postorder traversal')
printPostorder(n1)
print('Level order traversal')
printLevelOrder(n1)

root = sortedArrayToBST([1,2,3,4,5,6,7])
h = getTreeHeight(root)
print('h = %s' % h)
printLevelOrder(root)
