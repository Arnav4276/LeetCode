class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c = 0
        for i in sentences:
            w = len(i.split(" "))
            c =max(c, w)
        return c