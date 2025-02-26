class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        """
         intiakize hashset set()
         if num is in hashset return true 
         else add to hashset 
         if no duplicates return false 
        
        """ 
        seen = set()

        for num in nums:
          if num in seen:
            return True 

          else:
            seen.add(num)

        return False 