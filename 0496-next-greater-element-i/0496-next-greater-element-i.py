class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []             
        next_greater = {}       

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        # Remaining elements in stack have no next greater element
        for num in stack:
            next_greater[num] = -1

        # Build the result for nums1 using the hashmap
        result = []
        for num in nums1:
            result.append(next_greater[num])
        return result


       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # result = []
        # for num in nums1:
        #     found = False
        #     for i in range(len(nums2)):
        #         if nums2[i] == num:
        #             for j in range(i + 1, len(nums2)):
        #                 if nums2[j] > num:
        #                     result.append(nums2[j])
        #                     found = True
        #                     break
        #             if not found:
        #                 result.append(-1)
        #             break
        # return result
