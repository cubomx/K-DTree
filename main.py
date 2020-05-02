''' Implementation of the K-D Tree algorithm to
    make search in more than one level, by the
    moment only in two dimensions
'''
from kdtree import kdtree, Node
from math import ceil
from copy import deepcopy as dp
SIZE = 0
MAX_DIMENSION = 0

def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.key)
        printInorder(root.right)

def orderByLevel(node, sortedNodes, isRight, level):
    global MAX_DIMENSION, SIZE
    SIZE += 1
    level_ = dp(level)
    if level_ ==  MAX_DIMENSION:
        level_ = 0
    s = sorted(sortedNodes, key=lambda x: x.key[level_])
    median = ceil(len(sortedNodes) / 2) - 1

    for i in sortedNodes:
        print(i.key)
    print("\n\n")
    node.isLeaf = False
    if isRight:
        node.right = sortedNodes[median]
        node = node.right
    else:
        node.left = sortedNodes[median]
        node = node.left
    if len(sortedNodes) > 1:
        if median > 1:
            orderByLevel(node, sortedNodes[0:median], False, level_ + 1)
        else:
            SIZE += 1
            node.left = sortedNodes[0]
        if len(sortedNodes) - median > 1:
            orderByLevel(node, sortedNodes[median + 1:], True, level_ + 1)
        else:
            SIZE += 1
            node.right = sortedNodes[0]
    return



def orderTree(sortedNodes, tree):
    global SIZE
    median = ceil (len(sortedNodes)/ 2) - 1
    tree = kdtree(sortedNodes[median])
    orderByLevel(tree.root, sortedNodes[0:median], False, 1)
    orderByLevel(tree.root, sortedNodes[median+1:], True, 1)
    print(SIZE)
    return tree

def orderNodes(nodes, tree):
    sortBy = sorted(nodes, key=lambda x: x.key[0])
    orderTree(sortBy, tree)

def main():
    tree = None
    file = open("numbers.txt", "r")
    data = file.read()
    lines = data.split("\n")
    nodes = []
    for node in lines:
        values = node.split(" ")
        for idx, val in enumerate(values): # No matters the dimension of values
            values[idx] = int(val)
        nodes.append(Node(values))
    global MAX_DIMENSION
    MAX_DIMENSION= len(nodes[0].key)
    orderNodes(nodes, tree)
    file.close()

if __name__ == "__main__":
    main()

