class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,v in enumerate(nums):
          cmp = target - v
          if cmp in hashmap:
            return [hashmap[cmp],i]
          else:
            hashmap[v] = i

        return []
          