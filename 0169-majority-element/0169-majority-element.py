class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = dict.get(nums[i],0)+1
        max_val=max(dict.values())
        for k,v in dict.items():
            if v == max_val:
                return k