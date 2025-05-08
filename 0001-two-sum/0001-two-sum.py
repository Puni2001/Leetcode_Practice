class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hash_map = {}

      for i,v in enumerate(nums):
        cmp = target - v 
        if cmp in hash_map:
          return [hash_map[cmp], i]
        
        hash_map[v] = i 

      return []
