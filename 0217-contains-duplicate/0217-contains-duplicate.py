class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        # Create a hashset 
        seen = set()

        for num in nums:
            # If element in hashset 
            if num in seen:
                return True 
            else:
                seen.add(num)

        return False