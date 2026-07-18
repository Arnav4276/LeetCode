class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        a = 0
        for ch in columnTitle:
            a = a * 26 + (ord(ch) - ord('A') + 1)
        return a