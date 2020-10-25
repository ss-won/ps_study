class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int(''.join(list(map(str, digits)))) + 1
        return list(map(int, str(digits)))