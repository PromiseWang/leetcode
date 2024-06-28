from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]

        num = 1
        top = 0
        left = 0
        right = n - 1
        bottom = n - 1
        for i in range((n + 1) // 2):
            # 从左到右
            for j in range(left, right):
                result[top][j] = num
                num += 1

            # 从上到下
            for j in range(top, bottom):
                result[j][right] = num
                num += 1

            # 从右到左
            for j in range(right, left, -1):
                result[bottom][j] = num
                num += 1

            # 从下到上
            for j in range(bottom, top, -1):
                result[j][left] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if n % 2 == 1:
            result[n // 2][n // 2] = n * n
        return result


s = Solution()
n = 3
print(s.generateMatrix(n))
