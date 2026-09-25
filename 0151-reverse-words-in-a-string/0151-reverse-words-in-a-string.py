class Solution(object):
    def reverseWords(self, s):
        words = s.split() 
        reverse = words[::-1]
        return " ".join(reverse)
        