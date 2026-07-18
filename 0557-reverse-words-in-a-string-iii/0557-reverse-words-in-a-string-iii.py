class Solution:
    def reverseWords(self, s: str) -> str:
        w1 = s.split()
        w2 = []
        for word in w1:
            rw = word[::-1]
            w2.append(rw)
        return " ".join(w2)