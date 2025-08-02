class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            found = False
            for i in range(len(nums2)):
                if nums2[i] == num:
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > num:
                            result.append(nums2[j])
                            found = True
                            break
                    if not found:
                        result.append(-1)
                    break
        return result
