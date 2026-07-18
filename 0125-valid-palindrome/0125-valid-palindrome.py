class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars = []
        
        for char in s:
            
            if char.isalnum():
                
                lower_char = char.lower()
                
                cleaned_chars.append(lower_char)
                
        reversed_chars = cleaned_chars[::-1]
        
        if cleaned_chars == reversed_chars:
            return True
        else:
            return False