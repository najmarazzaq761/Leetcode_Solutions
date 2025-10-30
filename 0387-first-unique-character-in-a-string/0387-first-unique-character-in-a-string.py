from collections import deque, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        queue = []
        
        for i, char in enumerate(s):
            if freq[char] == 1:
                queue.append([char, i])
        
        if queue:
                return queue[0][1]
        else:
                return -1  
        











# queue = deque()  #  Clear intent: This is a FIFO queue
# queue = []       #  Ambiguous: Could be stack, list, or queue?             
# # Scenario: We need to remove from front (like in the earlier MinStack approach)

# # With regular list - POOR PERFORMANCE:
# queue.pop(0)           #  O(n) - all elements must shift!

# # With deque - EXCELLENT PERFORMANCE:  
# queue.popleft()        #  O(1) - constant time
