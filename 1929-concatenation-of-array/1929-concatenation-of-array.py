class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums + nums
        # return ans
         

        ans = []
        for _ in range(2):
            for num in nums:
                ans.append(num)
        return ans
        