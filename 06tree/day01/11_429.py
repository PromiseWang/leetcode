from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque()
        result = []
        queue.append(root)
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue.popleft()
                temp.append(node.val)
                for i in node.children:
                    if i:
                        queue.append(i)
            result.append(temp)
        return result


s = Solution()
