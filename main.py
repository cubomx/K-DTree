''' Implementation of the K-D Tree algorithm to
    make search in more than one level, by the
    moment only in two dimensions
'''
from kdtree import kdtree, Node
from math import ceil
from copy import deepcopy as dp

SIZE = 0
MAX_DIMENSION = 0
LIST = []


def printInorder(root):
    # Print the tree in inorder  (to the left of the left and then, right)
    if root:
        printInorder(root.left)
        print(root.key)
        printInorder(root.right)


def orderByLevel(node, sortedNodes, isRight, level):
    global MAX_DIMENSION, SIZE, LIST

    level_ = dp(level)
    if level_ == MAX_DIMENSION:  # verify the current level of the K-D Tree
        level_ = 0
    # order by the level of the K-D Tree
    s = sorted(sortedNodes, key=lambda x: x.key[level_])

    # get the element that it would enter to the tree and divided it
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
        # continue ordering both sides
        orderByLevel(node, s[0:median], False, level_ + 1)
        orderByLevel(node, s[median + 1:], True, level_ + 1)
    if len(s) == 2:  # if only 2 left, so the other obviously is at the right of it
        node.right = s[-1]
        SIZE += 1
        LIST.append(s[-1])
    return


def orderNodes(nodes, tree):
    sortBy = sorted(nodes, key=lambda x: x.key[0])  # order by x
    orderTree(sortBy, tree)
    return tree


def orderTree(sortedNodes, tree):
    global SIZE, LIST
    median = ceil(len(sortedNodes) / 2) - 1  # get the root by being in the middle of x-order
    tree = kdtree(sortedNodes[median])
    orderByLevel(tree.root, sortedNodes[0:median], False, 1)  # search in both sides
    orderByLevel(tree.root, sortedNodes[median + 1:], True, 1)
    printInorder(tree.root)
    return tree


def find_initial(tree, mins, maxs):
    # TODO: find the first node that has within all the values
    return tree.root


def search(tree, mins, maxs):
    explorer = find_initial(tree, mins, maxs)
    level = 1
    explorer = explorer.left
    ''' 
        TODO: Do the search by level 
    '''
    return


def main():
    tree = None
    file = open("numbers.txt", "r")
    data = file.read()
    lines = data.split("\n")
    nodes = []
    for node in lines:
        values = node.split(" ")
        for idx, val in enumerate(values):  # No matters the dimension of values
            values[idx] = int(val)
        nodes.append(Node(values))
    global MAX_DIMENSION
    MAX_DIMENSION = len(nodes[0].key)
    tree = orderNodes(nodes, tree)
    file.close()


if __name__ == "__main__":
    main()
