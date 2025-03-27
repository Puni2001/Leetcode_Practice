class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find the candidate for the dominant element using Boyer-Moore
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                count += 1 if candidate == num else -1
        
        # Step 2: Verify if the candidate is the actual dominant
        total_count = 0
        for num in nums:
            if num == candidate:
                total_count += 1
        n = len(nums)
        if total_count * 2 <= n:  # Not a dominant element
            return -1
        
        # Step 3: Check each possible split
        left_count = 0
        for i in range(n):
            if nums[i] == candidate:
                left_count += 1
            right_count = total_count - left_count
            left_size = i + 1
            right_size = n - left_size
            if left_size > 0 and right_size > 0:
                if left_count * 2 > left_size and right_count * 2 > right_size:
                    return i
        return -1