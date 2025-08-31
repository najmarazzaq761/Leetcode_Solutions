class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        # negatives and numbers ending with 0 (but not 0 itself) are not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # For even digits → x == reversed_num
        # For odd digits → x == reversed_num // 10
        return x == reversed_num or x == reversed_num // 10
