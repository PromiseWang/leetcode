import queue
from typing import List
from collections import deque


class Solution:
    class MonotoneQueue:
        def __init__(self):
            self.queue = deque()

        def push(self, x):
            # 1. 如果x > self.queue[-1], 则不断从右侧出队, 直到x <= self.queue[-1]
            while self.queue and x > self.queue[-1]:
                self.queue.pop()
            # 2. 否则, x直接入队
            self.queue.append(x)

        def pop(self, x):
            # 如果窗口移除的元素等于单调队列出口的元素, 那么单调队列弹出元素.
            # 否则不用任何操作
            if x == self.queue[0] and self.queue:
                return self.queue.popleft()

        def front(self):
            return self.queue[0]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = self.MonotoneQueue()
        result = []

        for i in range(k):
            q.push(nums[i])
        result.append(q.front())
        for i in range(k, len(nums)):
            q.pop(nums[i - k])
            q.push(nums[i])
            result.append(q.front())
        return result


solution = Solution()
# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
nums = [1, -1]
k = 1
print(solution.maxSlidingWindow(nums, k))
