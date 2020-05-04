class kdtree():
    def __init__(self, root):
        self.root = root

class Node():
    def __init__(self, values):
        self.key = values #it must be an array (if you want more level search)
        self.left = None
        self.right = None
        self.isLeaf = True

    def __str__(self):
        return self.key  # print the key as an array value

