class Solution:
    def maxSelectedElements(self, A: List[int]) -> int:
        dp = defaultdict(int)
        A.sort()
        for a in A:
            dp[a + 1] = dp[a] + 1
            dp[a] = dp[a - 1] + 1
        return max(dp.values())