class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        list1=[]
        count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                list1.append(count)
                count =0
        list1.append(count)
        return max(list1)