from typing import List, Optional

from utils.tree.binary_tree import TreeNode


class Solution:
    """
    使用迭代的方式得到结果
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        p = root
        while p is not None or len(stack) != 0:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack[-1]
                stack.pop()
                result.append(p.val)
                p = p.right
        return result


s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(s.inorderTraversal(root))
