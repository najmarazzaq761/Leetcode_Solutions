class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        temp = []
        result = []
        n = len(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1

        def backtrack(temp):
            if len(temp) == n:
                result.append(temp.copy())
                return
            for num in freq:
                if freq[num] == 0:
                    continue
                temp.append(num)
                freq[num]-=1
                backtrack(temp)
                
                temp.pop()
                freq[num]+=1
        backtrack([])
        return result


