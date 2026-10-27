class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def generate(cur, left, right):
            if n == left == right:
                res.append(cur[:])
            
            if left < n:
                generate(cur + "(", left + 1, right)
            
            if right < left:
                generate(cur + ")", left, right + 1)

        generate("", 0, 0)

        return res


        
