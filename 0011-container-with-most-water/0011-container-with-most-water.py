class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        max_area = 0
        while start < end:
            h = min(height[start], height[end])
            w = end - start
            area = h * w
            if area > max_area:
                max_area = area
            if height[start] < height[end]:
                start += 1

            else:
                end -= 1
        return max_area