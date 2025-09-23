class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums:
            if num < ans:
                ans = num
        return ans
