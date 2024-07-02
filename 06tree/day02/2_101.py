from typing import List, Optional
from utils.tree.binary_tree import TreeNode


class Solution:
    def func(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        elif left.val == right.val:
            if not self.func(left.left, right.right):
                return False
            if not self.func(left.right, right.left):
                return False
            return True
        else:
            return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        elif root.left and root.right:
            return self.func(root.left, root.right)
        elif root.left is None and root.right is None:
            return True
        else:
            return False


s = Solution()

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# print(s.isSymmetric(root))


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(4)
# print(s.isSymmetric(root))

root = TreeNode(1)
print(s.isSymmetric(root))