class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # i = 0
        # count = 0
        # j = len(nums) - 1
        # while i < j:
        #     if (nums[i] + nums[j]) == k:
        #         i+=1
        #         j-=1
        #         count += 1
        #     elif nums[i] + nums[j] < k:
        #         i+=1
        #     else:
        #         j-=1
        # return count
       
        count = 0
        freq = {}

        for num in nums:
            complement = k - num

            if freq.get(complement,0) > 0:
                count += 1
                freq[complement] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1

        return count

        
            