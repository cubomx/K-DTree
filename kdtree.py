class kdtree():
    def __init__(self, root):
        self.root = root



    def printTree(self):
        root = self.root
        if not root.isLeaf:
            if not root.left is None:
                self.search(root.left)
            if not root.right is None:
                self.search(root.right)


class Node():
    def __init__(self, values):
        self.key = values #it must be an array (if you want more level search)
        self.left = None
        self.right = None
        self.isLeaf = True

    def __str__(self):
        return self.key

