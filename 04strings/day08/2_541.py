class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # new_s = ""
        # for i in range(0, len(s), 2 * k):
        #     if i + k > len(s):
        #         new_s += s[i:][::-1]
        #     else:
        #         new_s += s[i:i + k][::-1]
        #     if i + 2 * k > len(s):
        #         new_s += s[i + k:]
        #     else:
        #         new_s += s[i + k:i + 2 * k]
        # return new_s
        list_s = list(s)
        for i in range(0, len(list_s), 2 * k):
            list_s[i:i + k] = reversed(list_s[i:i + k])
        return "".join(list_s)


solution = Solution()
s = "abcdefg"
print(solution.reverseStr(s, 2))
