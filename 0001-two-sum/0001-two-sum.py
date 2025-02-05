class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,val in enumerate(nums):
            complement = target - val
            if complement in hashmap:
                return [hashmap[complement],i]

            else:
                hashmap[val] = i