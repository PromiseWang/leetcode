from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_length = 100001
        sum = 0
        while len(nums) >= right >= left:
            if sum < target:
                if right < len(nums):
                    sum += nums[right]
                    right += 1
                else:
                    break
            else:
                if min_length > right - left:
                    min_length = right - left
                sum -= nums[left]
                left += 1

        if min_length == 100001:
            return 0
        else:
            return min_length


s = Solution()
nums = [2,3,1,2,4,3]
target = 7

print(s.minSubArrayLen(target, nums))
