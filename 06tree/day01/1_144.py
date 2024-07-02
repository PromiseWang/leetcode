from utils.tree.binary_tree import TreeNode
from typing import List, Optional


class Solution:
    """
    使用递归的方式得到结果
    """
    def pre(self, root: Optional[TreeNode], result: List[int]):
        result.append(root.val)
        if root.left:
            self.pre(root.left, result)
        if root.right:
            self.pre(root.right, result)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        self.pre(root, result)
        return result


s = Solution()

root = None
print(s.preorderTraversal(root))

# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# print(s.preorderTraversal(root))
