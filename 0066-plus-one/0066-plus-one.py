class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num_str = ""
        for digit in digits:
            num_str += str(digit)
            
        number = int(num_str)
        
        number += 1
        
        result = []
        for char in str(number):
            result.append(int(char))
            
        return result