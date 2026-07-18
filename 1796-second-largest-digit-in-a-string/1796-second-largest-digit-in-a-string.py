class Solution:
    def secondHighest(self, s: str) -> int:
        l1 = []
        for i in s:
            if i.isdigit():
                l1.append(i)
        l2 = sorted(set(l1))
        if len(l2) >= 2:
            a = l2[-2]
            b = int(a)
            return b
        else:
            return (-1)