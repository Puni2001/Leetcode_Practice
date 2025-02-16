class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        nums should be sorted 
        use 2 ptr left = 0 , right = len(nums) - 1
        mid = ( left + right ) // 2
        loop through nums 
        if mid == target 
            return its index
        elif mid < target 
            left mid + 1  # if its less than target no points to check half we can move from next element 
        else 
            right mid - 1  # if its greater than target right to next elemt 
               
        """
        left , right = 0 , len(nums)-1
        while left <= right:
            mid = ( left + right ) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1