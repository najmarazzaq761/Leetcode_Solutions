class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # result=0
        # for num in nums:
        #     result ^= num
        # return result

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             i+=1
        #         else:
        #             j+=1
        #     return nums[i]

        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]