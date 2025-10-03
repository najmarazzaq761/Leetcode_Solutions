class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_sofar = nums[0]
        min_sofar = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if n<0:
                max_sofar, min_sofar = min_sofar, max_sofar
            max_sofar = max(n, max_sofar*n)
            min_sofar = min(n, min_sofar*n)
            result = max(result, max_sofar)
        return result
            
