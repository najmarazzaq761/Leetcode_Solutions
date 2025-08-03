class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        for c in columnTitle:
            char=ord(c)-ord('A')+1
            result=result*26+char
        return result