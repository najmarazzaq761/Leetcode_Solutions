class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
            
        count=duration
        for i in range(1,len(timeSeries)):
             diff = (timeSeries[i] - timeSeries[i-1])
             if diff >=duration:
                    count+=duration
             else:
                        count+=diff
        return count
                