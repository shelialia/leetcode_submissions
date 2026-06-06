class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = float("-inf")

        while left < right:
            minHeight = min(height[left], height[right])
            curArea = minHeight * (right - left)
            maxArea = max(maxArea, curArea)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return maxArea