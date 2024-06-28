from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        if nums[0] > 0:
            return results
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1
                elif temp > 0:
                    right -= 1
                else:
                    left += 1
        return results


s = Solution()
nums = [0, 0, 0, 0]
print(s.threeSum(nums))
