class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
            maximum  = max(candies)
            for i in range(len(candies)):
                candies[i] = candies[i]+ extraCandies >= maximum
            return candies