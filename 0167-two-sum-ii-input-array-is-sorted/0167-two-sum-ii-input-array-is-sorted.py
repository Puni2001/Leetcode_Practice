class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,v in enumerate(numbers):
            c = target - v
            if c in hashmap:
                return [hashmap[c],i+1]
            
            hashmap[v] = i + 1
        
        return []