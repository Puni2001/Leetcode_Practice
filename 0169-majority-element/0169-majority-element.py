class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        half = len(nums)/2

        count = Counter(nums)

        for num in nums:
            if count[num] > half:
                return num