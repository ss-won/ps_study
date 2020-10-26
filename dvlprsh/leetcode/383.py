class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote in magazine:
            return True
        magazine = list(magazine)
        for v in ransomNote:
            if v in magazine:
                magazine.remove(v)
            else:
                return False
        return True