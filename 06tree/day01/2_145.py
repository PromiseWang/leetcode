from typing import List, Optional
from utils.tree.binary_tree import TreeNode


class Solution:
    """
    使用递归的方式得到结果
    """

    def post(self, root: Optional[TreeNode], result: List[int]):
        if root.left:
            self.post(root.left, result)
        if root.right:
            self.post(root.right, result)
        result.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        self.post(root, result)
        return result


s = Solution()
