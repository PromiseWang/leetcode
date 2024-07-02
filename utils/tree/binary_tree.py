from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    pass


if __name__ == '__main__':
    root = TreeNode(0)

    node1 = TreeNode(1)
    root.left = node1

    node2 = TreeNode(2)
    root.right = node2

    print(root)
