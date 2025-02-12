class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index,current_subset):
            # base case 
            if index == len(nums):
                result.append(current_subset[:])
                return

            # include nums[index]
            current_subset.append(nums[index])
            backtrack(index+1, current_subset)

            # exclude nums[index] or remove or backtrack
            current_subset.pop()
            backtrack(index+1, current_subset)
        
        backtrack(0,[])

        return result 