class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
  # Step 1: Count the frequency of each element in nums
        count = {}
        for val in nums:
            count[val] = 1 + count.get(val, 0)
        # Example state of 'count': {1: 3, 2: 2, 3: 1}

        # Step 2: Use the frequency count to populate the buckets
        arr = [[] for i in range(len(nums) + 1)]  # Array of empty lists to act as buckets
        for n, c in count.items():
            arr[c].append(n)
        # Example state of 'arr': [[], [3], [2], [1], [], [], []]

        # Step 3: Collect the top k frequent elements from the buckets
        res = []
        for i in range(len(arr) - 1, 0, -1):  # Iterate from the highest possible frequency to the lowest
            for j in arr[i]:  # Iterate through all elements with the current frequency
                res.append(j)
                if len(res) == k:  # If we have collected k elements, return the result
                    return res
        