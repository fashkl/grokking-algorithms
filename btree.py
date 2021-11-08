class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)


def printOriginalTree(root):
    if root is None:
        return
    print(root.value)
    print(root.left.value)
    print(root.left.left.value)
    print(root.left.right.value)
    print(root.right.value)

    # if root.left is not None:
    #     print()


def flipTree(root):
    if root:
        print(root.value)

        root.left, root.right = root.right, root.left

        flipTree(root.left)
        flipTree(root.right)


# printOriginalTree(root,"\n")
# 0 2 1 4 3
flipTree(root)
