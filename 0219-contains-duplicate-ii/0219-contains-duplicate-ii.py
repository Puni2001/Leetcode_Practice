class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        mp = {}
      #  n = len(nums)
        for i,num in enumerate(nums):
            
            if num in mp and i-mp[num] <= k:
                return True 

            else:
                mp[num] = i

        return False
                

           
            

            