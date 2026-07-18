class Solution:
    def largestEven(self, s: str) -> str:
        for i in range(len(s) - 1, -1, -1):
            if int(s[i]) % 2 == 0:  # check even
                return s[:i+1]
        return ""