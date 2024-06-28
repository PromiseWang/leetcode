from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = []
        for i in set1:
            if i in nums2:
                result.append(i)
        return result

