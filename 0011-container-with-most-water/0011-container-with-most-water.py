class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area = length * breadth 
        # max length and max breadth 
        max_area = 0 
        left , right = 0 , len(height) - 1

        while left < right:
            current_area = min(height[left], height[right])  * (right - left )

            max_area = max(current_area, max_area)

            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1
        return max_area 