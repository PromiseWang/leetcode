class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


solution = Solution()
s = "the sky is blue"
print(solution.reverseWords(s))
