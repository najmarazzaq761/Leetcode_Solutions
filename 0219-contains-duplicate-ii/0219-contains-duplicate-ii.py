# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         seen={}
#         for i,num in enumerate(nums):
#             if num in seen and i-seen[num]<=k:
#                 return True
        
#             seen[num]=i
            
#         return False
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()  # elements inside the sliding window

        left = 0  # left pointer of the window

        for right in range(len(nums)):
            
            # If nums[right] already exists in window, duplicate found
            if nums[right] in window:
                return True

            # Add current number into window
            window.add(nums[right])

            # Keep window size ≤ k
            if right - left >= k:
                window.remove(nums[left])
                left += 1

        return False
