from collections import deque, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        queue = []
        
        for i, char in enumerate(s):
            if freq[char] == 1:
                queue.append((char, i))
        
    
        # return queue[0][1] if queue else -1
        if queue:
            return queue[0][1]
        else:
            return -1 
            