class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      hash_map = {}

      # target = x + value 

      for index , value in enumerate(nums):
        complement = target - value 
        if complement in hash_map:
          return [hash_map[complement], index]

        hash_map[value] = index 

      return []
