class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Length of the nums 
        len_nums = len(nums)
        # Need store output result
        output = [1] * len_nums

        # Prefix prd all to left 
        prefix = 1
        for i in range(len_nums):
            output[i] = prefix
            prefix *= nums[i] # update the running prefix 

        # suffix prod all to right and combine with prefix
        suffix = 1
        for i in range(len_nums-1, -1,-1):
            output[i] *= suffix # combine prefix 
            suffix *= nums[i] # update the suffix 

        return output 
        


        
        