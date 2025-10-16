class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(0, len(nums) - 1, 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]


        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        #     if count == 1:
        #         return nums[i]


        # result=0
        # for num in nums:
        #     result ^= num
        # return result


        count = Counter(nums)
        for num, freq in count.items():
            if freq == 1:
                return num