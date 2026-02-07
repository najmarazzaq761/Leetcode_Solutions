class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        second = 0
        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
        return (first-1)*(second-1)

        # nums.sort()
        # return (nums[-2] - 1) * (nums[-1] - 1)


        # product = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         new_pro = (nums[i]-1)*(nums[j]-1)
        #         product = max(product, new_pro)
        # return product
            


            

             


            