class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        a = {}
        b = {}
        for p, w in zip(pattern, words):
            if p in a and a[p] != w:
                return False

            if w in b and b[w] != p:
                return False

            a[p] = w
            b[w] = p
        
        return True