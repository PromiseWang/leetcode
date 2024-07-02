from utils.tree.binary_tree import TreeNode
from typing import List, Optional


class Solution:
    """
    使用迭代的方式得到结果
    """

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
            result.append(temp.val)
        # print(result)
        return result


s = Solution()

# root = None
# print(s.preorderTraversal(root))

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.preorderTraversal(root))

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# print(s.preorderTraversal(root))
