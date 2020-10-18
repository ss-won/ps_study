class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = int(''.join(list(str(x))[::-1]))
        return reversed_x == x