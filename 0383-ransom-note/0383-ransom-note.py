
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch in magazine:
                magazine=magazine.replace(ch,'',1)
            else:
                return False
        return True
    