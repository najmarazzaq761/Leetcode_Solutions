from collections import deque, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # freq = Counter(s)
        # queue = deque()
        
        # for i, char in enumerate(s):
        #     if freq[char] == 1:
        #         queue.append((char, i))
        
        # if queue:
        #         return queue[0][1]
        # else:
        #         return -1  

    
        queue = []        
        count = {}         
        front = 0       
        for i, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            queue.append((ch, i))   

            
            while front < len(queue) and count[queue[front][0]] > 1:
                front += 1   

        
        return queue[front][1] if front < len(queue) else -1
        











# queue = deque()  #  Clear intent: This is a FIFO queue
# queue = []       #  Ambiguous: Could be stack, list, or queue?             
# # Scenario: We need to remove from front (like in the earlier MinStack approach)

# # With regular list - POOR PERFORMANCE:
# queue.pop(0)           #  O(n) - all elements must shift!

# # With deque - EXCELLENT PERFORMANCE:  
# queue.popleft()        #  O(1) - constant time
