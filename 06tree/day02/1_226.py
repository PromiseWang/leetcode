from typing import List, Optional
from utils.tree.binary_tree import TreeNode


class Solution:
    def pre(self, root: Optional[TreeNode]):
        root.left, root.right = root.right, root.left
        if root.left:
            self.pre(root.left)
        if root.right:
            self.pre(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return []
        self.pre(root)
        return root


s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
s.invertTree(root)
print(s)
