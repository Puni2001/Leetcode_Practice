class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        nums[i] == nums[i+1]  -> nums[i] * 2
        replace -> nums[i+1] -> 0
        move all zero to end         
        """
        n = len(nums)-1
        for i in range(n):
          if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0

        left = 0 
        for right in range(len(nums)):
          if nums[right] != 0:
            nums[right] , nums[left] = nums[left] , nums[right]

            left += 1
        
        return nums

            


        return nums