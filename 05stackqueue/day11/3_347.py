import collections
import heapq
from queue import PriorityQueue
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i, 0) + 1
        # sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        # result = []
        # for i in range(k):
        #     result.append(sorted_d[i][0])
        # return result
        count = collections.Counter(nums)
        heap = [(freq, num) for num, freq in count.items()]
        return [item[1] for item in heapq.nlargest(k, heap)]



solution = Solution()
# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# nums = [-1, -1]
# k = 1
nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
print(solution.topKFrequent(nums, k))
