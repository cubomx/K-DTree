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
    tree = orderTree(sortBy, tree)
    return tree


def orderTree(sortedNodes, tree):
    global SIZE, LIST
    median = ceil(len(sortedNodes) / 2) - 1  # get the root by being in the middle of x-order
    tree = kdtree(sortedNodes[median])
    orderByLevel(tree.root, sortedNodes[0:median], False, 1)  # search in both sides
    orderByLevel(tree.root, sortedNodes[median + 1:], True, 1)
    #printInorder(tree.root)
    return tree

def on_range(node, mins, maxs):
    isOnRange = True
    for idx, limit in enumerate(mins):
        if node.key[idx] >= mins[idx] and node.key[idx] <= maxs[idx]:
            continue
        else:
            isOnRange = False
            break
    return isOnRange

def find_initial(tree, mins, maxs):
    global MAX_DIMENSION
    level = 0
    while True:
        if MAX_DIMENSION == level:
            level = 0
        if tree:
            if tree.key[level] >= mins[level] and tree.key[level] <= maxs[level]:
                return tree
            if tree.key[level] > maxs[level]:
                tree = tree.left
            if tree.key[level] < mins[level]:
                tree = tree.right
            level += 1
    return tree

def search_sons(node, level, mins, maxs):
    global MAX_DIMENSION
    level_ = dp(level)
    if MAX_DIMENSION == level_:
        level_ = 0
    if node:
        if node.key[level_] >= mins[level_] and node.key[level_] <= maxs[level_]:
            if on_range(node, mins, maxs): print(node.key)
            search_sons(node.right, level_ + 1, mins, maxs)
            search_sons(node.left, level_ + 1, mins, maxs)
        if node.key[level_] > maxs[level_]:
            search_sons(node.left, level_ + 1, mins, maxs)
        if node.key[level_] < mins[level_]:
            search_sons(node.right, level_ + 1, mins, maxs)

def search(tree, mins, maxs):
    explorer = find_initial(tree.root, mins, maxs)
    if on_range(explorer, mins, maxs):
        print(explorer.key)
    level = 1
    search_sons(explorer.left, level, mins, maxs)
    search_sons(explorer.right, level, mins, maxs)

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
    ''' 
    In both arrays [minimum values] [maximum values], the first element is the x limit, and y limit and continues
    till the dimensions of the K-D Tree
    '''
    search(tree, [50, 20], [90, 90])
    file.close()


if __name__ == "__main__":
    main()
