from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        d = {}
        for i in nums1:
            for j in nums2:
                d[i + j] = d.get(i + j, 0) + 1

        for i in nums3:
            for j in nums4:
                if -(i + j) in d:
                    count += d[-(i + j)]
        return count


s = Solution()
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
print(s.fourSumCount(nums1, nums2, nums3, nums4))
