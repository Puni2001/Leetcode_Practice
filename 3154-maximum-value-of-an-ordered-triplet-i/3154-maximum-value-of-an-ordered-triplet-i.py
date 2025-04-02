class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_triplet = 0

        for i in range(n):
          for j in range(i+1,n):
            for k in range(j+1,n):

              current_triplet = (nums[i] - nums[j])*nums[k]
              max_triplet = max(current_triplet, max_triplet)

        return max_triplet