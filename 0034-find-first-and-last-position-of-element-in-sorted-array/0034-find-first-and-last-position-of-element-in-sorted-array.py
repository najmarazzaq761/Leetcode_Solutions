class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occurance = -1
        last_occurance = -1
        # left, right = 0,len(nums)-1
        # while left <= right:
        #     mid = (left+right)//2
        #     if target == nums[mid]:
        #         first_occurance = mid
        #         right = mid -1
        #     elif target < nums[mid]:
        #         right = mid -1
        #     else:
        #         left = mid + 1


        # left , right = 0, len(nums)-1
        # while left <= right:
        #     mid = (left+right)//2
        #     if target == nums[mid]:
        #         last_occurance = mid
        #         left = mid + 1
        #     elif target < nums[mid]:
        #         right = mid -1
        #     else:
        #         left = mid + 1

        # return [first_occurance, last_occurance]
        for i in range(len(nums)):
            if nums[i] == target:
                first_occurance = i
                break

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                last_occurance = i
                break
        return [first_occurance, last_occurance]
            