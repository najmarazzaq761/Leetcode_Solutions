class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        res = s
        for right in range(1, len(nums)):
            # resetting sum to the current element when sum becomes less than 0
            if s < 0:
                s = nums[right]
            # otherwise add the current element with the previous sum
            else:
                s += nums[right]
            # update maximum(res) 
            if s > res:
                res = s
        return res