class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            reversed_int = int(str(-x)[::-1])
            reversed_int = -reversed_int
        else:
            reversed_int = int(str(x)[::-1])
            
        if reversed_int < -2147483648 or reversed_int > 2147483647:
            return 0
        else:
            return reversed_int