from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
            mid = (left + right) // 2
        return -1


s = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(s.search(nums, target))
