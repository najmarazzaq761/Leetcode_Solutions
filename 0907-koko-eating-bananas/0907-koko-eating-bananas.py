class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left + right)//2
            hours = 0

            for p in piles:
                hours += (p//mid) + (1 if p%mid != 0 else 0)

            if hours <= h:
                result = min(result,  mid)
                right = mid - 1
            else:
                left = mid + 1
        return result