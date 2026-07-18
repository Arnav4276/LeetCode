class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        l1 = len(candyType)//2
        l2 = len(set(candyType))
        return min(l1,l2)