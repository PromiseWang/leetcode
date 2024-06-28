from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            if target - v in d and d[target - v] != i:
                return [d[target - v], i]
            else:
                d[v] = i


print(Solution().twoSum([3, 3], 6))
