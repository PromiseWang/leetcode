from collections import deque
from typing import List, Optional

from utils.tree.binary_tree import TreeNode

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        queue = deque()
        result = []
        queue.append(root)
        while queue:
            n = len(queue)
            temp = 0
            for i in range(n):
                node = queue.popleft()
                temp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(round(temp/n, 5))
        return result


s = Solution()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(s.averageOfLevels(root))
