class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_set=set(nums1)
        ans=set()
        for i in range(len(nums2)): 
            if nums2[i] in hash_set:
                ans.add(nums2[i])
        return list(ans)