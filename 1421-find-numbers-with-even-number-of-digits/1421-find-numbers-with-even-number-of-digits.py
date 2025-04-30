class Solution:
    def findNumbers(self, nums: List[int]) -> int:
      if not nums:
        return 0
      count = 0
      for num in nums:
        if len(str(num)) % 2 == 0:
          count += 1
      
      return count