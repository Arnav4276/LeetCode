class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        p = 0
        x1 = x
        while x>0:
            a = x%10
            p = (p*10)+a
            x = x//10
            
        return x1==p