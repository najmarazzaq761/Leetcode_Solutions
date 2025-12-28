class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # nums.sort()
           # bubble sort
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[j] < nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]

              # merge sort
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result        

        nums = merge_sort(nums)
        l = 0
        r = k - 1
        n = len(nums)
        res = float("inf")
        while r < n:
            res = min(res, nums[r] - nums[l])
            l+=1
            r+=1
        return res
