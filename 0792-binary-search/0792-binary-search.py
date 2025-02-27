class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            [-1,0,3,5,9,12]
              l          r 

              mid = (l + r) // 2 
              is num[mid] == target 
                return index 
              nums[mid] < target:
                left = mid + 1 
                else right = mid + 1

        """
        left , right = 0 , len(nums) - 1

        while left<= right:

          mid = (left + right) // 2

          if nums[mid] == target:
            return mid 

          elif nums[mid] < target:
            left = mid + 1
          else:
            right = mid - 1

        return -1


          