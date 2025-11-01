class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        res = s
        for right in range(1,len(nums)):
            if s<0:
                s = nums[right]
            else:
                s+= nums[right]
            if s> res:
                res = s
        return res
        # res = nums[0]
        # for i in range(1, len(nums)):
        #     s = max(nums[i], s+nums[i])
        #     res = max(res, s)
        # return res