class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        if not nums:
          return []
        for i in range(len(nums)):
          ans.append(nums[nums[i]])
        
        return ans