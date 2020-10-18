class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        isNegative = False
        
        if x[0] == '-':
            x = x[1:]
            isNegative = True
            
        x = int(''.join(x[::-1]))
        
        if isNegative:
            x *= (-1)

        if x < (-1) * 2 ** 31 or x >= 2 ** 31:
            return 0
        
        return x