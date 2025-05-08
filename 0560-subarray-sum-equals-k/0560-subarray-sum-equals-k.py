class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res =  0
        curr = 0 
        hashmap = defaultdict(int)
        hashmap[0] =  1

        for num in nums:
          curr += num
          res += hashmap[curr-k]
          hashmap[curr] += 1
        
        return res 