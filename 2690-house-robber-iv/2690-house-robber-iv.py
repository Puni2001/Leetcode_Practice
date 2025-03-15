class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # 'k' check function
        def robCapability(cap):
            count = 0
            i = 0 
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2  # Skip the adjacent house
                else:
                    i += 1  # Move to the next house
            return count >= k

        # Binary Search
        left = min(nums)
        right = max(nums)

        while left < right:
            mid = (left + right) // 2
            if robCapability(mid):  # Use 'mid' here instead of 'min'
                right = mid
            else:
                left = mid + 1
        return left