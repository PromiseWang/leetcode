from typing import List, Optional

from utils.tree.binary_tree import TreeNode


class Solution:
    """
    使用递归的方式得到结果
    """

    def inorder(self, root: Optional[TreeNode], result: List[int]):
        if root.left:
            self.inorder(root.left, result)
        result.append(root.val)
        if root.right:
            self.inorder(root.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        self.inorder(root, result)
        return result


s = Solution()
