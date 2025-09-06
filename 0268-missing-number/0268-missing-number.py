class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    #    n = len(nums)
    #    expected_sum = n*(n+1)//2
    #    actual_sum = sum(nums)
    #    return expected_sum - actual_sum
         for i in range(0, len(nums)+1):
            if i not in nums:
                return i 