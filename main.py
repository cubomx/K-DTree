''' Implementation of the K-D Tree algorithm to
    make search in more than one level, by the
    moment only in two dimensions
'''
from kdtree import kdtree, Node
from math import ceil
from copy import deepcopy as dp
SIZE = 0
MAX_DIMENSION = 0
LIST= []
def printInorder(root):
    if root:

        printInorder(root.right)
        print(root.key)


def orderByLevel(node, sortedNodes, isRight, level):
    global MAX_DIMENSION, SIZE, LIST

    level_ = dp(level)
    if level_ ==  MAX_DIMENSION:
        level_ = 0
    s = sorted(sortedNodes, key=lambda x: x.key[level_])
    '''for i in s:
        print(i.key)
    print("\n\n")'''

    median = ceil(len(sortedNodes) / 2) - 1
    LIST.append(s[median])
    node.isLeaf = False
    if isRight:
        node.right = s[median]
        node = node.right
        SIZE += 1
    else:
        node.left = s[median]
        node = node.left
        SIZE += 1

    if len(s) > 2:
        orderByLevel(node, s[0:median], False, level_ + 1)
        orderByLevel(node, s[median + 1:], True, level_ + 1)
    if len(s) == 2:
        node.right = s[-1]
        SIZE += 1
        LIST.append(s[-1])
    return



def orderTree(sortedNodes, tree):
    global SIZE, LIST
    median = ceil (len(sortedNodes)/ 2) - 1
    tree = kdtree(sortedNodes[median])
    orderByLevel(tree.root, sortedNodes[0:median], False, 1)
    orderByLevel(tree.root, sortedNodes[median+1:], True, 1)
    for i in LIST:
        print(i.key)
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

