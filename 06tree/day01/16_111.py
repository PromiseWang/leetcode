from typing import List, Optional
from collections import deque
from utils.tree.binary_tree import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left is None and node.right is None:
                    return depth
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return depth


s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
print(s.minDepth(root))

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(s.minDepth(root))

# root = TreeNode(2)
# root.right = TreeNode(3)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(5)
# root.right.right.right.right = TreeNode(6)
# print(s.minDepth(root))
