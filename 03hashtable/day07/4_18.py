from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while nums[right] == nums[right - 1] and right > left:
                            right -= 1
                        while nums[left] == nums[left + 1] and right > left:
                            left += 1
                        left += 1
                    elif temp < target:
                        left += 1
                    else:
                        right -= 1
        return result


s = Solution()
# nums = [1, 0, -1, 0, -2, 2]
target = -11
nums = [1, -2, -5, -4, -3, 3, 3, 5]

print(s.fourSum(nums, target))
