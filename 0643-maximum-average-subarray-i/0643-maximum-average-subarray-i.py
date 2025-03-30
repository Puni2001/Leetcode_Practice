class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
      n = len(nums)
          
      # Step 1: Compute the initial window sum (first k elements)
      window_sum = sum(nums[:k])
      max_sum = window_sum  # Initialize max sum

      # Step 2: Slide the window across the array
      for i in range(k, n):
          window_sum += nums[i] - nums[i - k]  # Add new element, remove old element
          max_sum = max(max_sum, window_sum)   # Update max sum if needed

      return max_sum / k  # Return the maximum average

