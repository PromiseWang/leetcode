from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = nums.copy()
        index = right
        while index >= 0:
            if nums[left] ** 2 <= nums[right] ** 2:
                result[index] = nums[right] ** 2
                right -= 1
            else:
                result[index] = nums[left] ** 2
                left += 1
            index -= 1
        return result


nums = [-7,-3,2,3,11]

print(Solution().sortedSquares(nums))
