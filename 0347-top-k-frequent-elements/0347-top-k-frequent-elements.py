from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: count frequency of each number
        freq = Counter(nums)   # hashmap {num: frequency}
        
        # Step 2: create buckets (index = frequency)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
        
        # Step 3: collect top k elements from high freq to low
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
