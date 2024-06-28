class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = [0 for _ in range(26)]
        d2 = [0 for _ in range(26)]
        for i in range(len(s)):
            d1[ord(s[i]) - 97] += 1
        for i in range(len(t)):
            d2[ord(t[i]) - 97] += 1
        return d1 == d2


s1 = "asdf"
s2 = "asdf"
s = Solution()
print(s.isAnagram(s1, s2))
