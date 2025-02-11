class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # This will store all the subsets we generate.

        def backtrack(start, path):
            # Each time we enter backtrack, we add the current path (subset) to result.
            result.append(path[:])  # Make a copy of the current subset and add it.

            # Now, we loop through all possible next elements starting from 'start'
            for i in range(start, len(nums)):
                path.append(nums[i])       # Choose nums[i] to be in the current subset.
                backtrack(i + 1, path)     # Recursively explore further subsets with nums[i] included.
                path.pop()                 # Remove the last added element to backtrack (undo the choice).

        backtrack(0, [])  # Start from index 0 with an empty subset.
        return result
