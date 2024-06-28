class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        def func(n):
            temp = n
            sum = 0
            while temp > 0:
                sum += (temp % 10) ** 2
                temp //= 10
            return sum
        sum = n
        while True:
            sum = func(sum)
            if sum == 1:
                return True
            if sum in s:
                return False
            else:
                s.add(sum)


print(Solution().isHappy(2))
