class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        half = len(nums)/2

        #count = Counter(nums)
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > half:
                return num