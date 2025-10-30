from collections import deque, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        queue = deque()
        
        for i, char in enumerate(s):
            if freq[char] == 1:
                queue.append((char, i))
        
        # The first element in our queue is the answer
        return queue[0][1] if queue else -1