class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        left = right = 0
        
        for ch in s:
            left += (ch == '(')
            right += (ch == ')')
            
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0
        
        left = right = 0
        for ch in reversed(s):
            left += (ch == '(')
            right += (ch == ')')
            
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0
        
        return max_len