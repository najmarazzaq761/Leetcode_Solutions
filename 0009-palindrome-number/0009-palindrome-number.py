class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        # negatives and numbers ending with 0 (but not 0 itself) are not palindrome
        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False
        
        # reversed_num = 0
        # while x > reversed_num:
        #     reversed_num = reversed_num * 10 + x % 10
        #     x //= 10
        
        # # For even digits → x == reversed_num
        # # For odd digits → x == reversed_num // 10
        # return x == reversed_num or x == reversed_num // 10
 # ---------------------------------------------------------
        rev = 0
        num = x
        while num>0:
            rev = rev*10 + num%10
            num //= 10
        if rev == x:
            return True
        return False




        # left = 0
        # x = str(x)
        # right = len(x)-1
        # for i in range(len(x)):
        #     if x[left] != x[right]:
        #         return False
        #     left+=1
        #     right-=1
        # return True
