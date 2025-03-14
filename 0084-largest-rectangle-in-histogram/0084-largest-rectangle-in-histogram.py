class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stores indices of bars
        max_area = 0
        heights.append(0)  # Add a dummy height to process all bars

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
