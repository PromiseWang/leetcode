class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if i == 0:
                stack.append(s[i])
            else:
                if len(stack) != 0 and s[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])

        return "".join(stack)


solution = Solution()

s = "abbaca"
print(solution.removeDuplicates(s))
