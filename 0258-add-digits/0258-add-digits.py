class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
             rem = num % 10
             qt = num // 10
             num = rem + qt 
        return num

 # separate and add those two numbers then again compare if still greater then 9 then add again 
        
        # while num >=10:
        #     res = 0
        #     while num > 0:
        #         res += num % 10
        #         num //= 10
        #     num = res
        # return num    
