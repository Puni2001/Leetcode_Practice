### Problem 217: Contains Duplicate


#### Problem Statement:
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.


**Example 1:**
- Input: `nums = [1, 2, 3, 1]`
- Output: `true`


**Example 2:**
- Input: `nums = [1, 2, 3, 4]`
- Output: `false`


**Example 3:**
- Input: `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`
- Output: `true`


**Constraints:**
- (1 leq text{nums.length} leq 10^5)
- (-10^9 leq text{nums[i]} leq 10^9)


#### Brute Force Solution


Let's start with the brute force approach. This is the simplest way to solve the problem by checking every pair of elements in the array to see if there are any duplicates. Here’s how it works:


```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
```


**Explanation:**
1. Loop through each element using index `i`.
2. For each element at index `i`, loop through the rest of the elements using index `j`.
3. Check if any pair of elements are equal.
4. If any pair is found to be equal, return `True`.
5. If no pairs are found to be equal after all iterations, return `False`.


**Time Complexity:** (O(n^2)) because we are using two nested loops.
**Space Complexity:** (O(1)) as we are not using any extra space.


#### Optimized Solution


Next, let's discuss a more efficient solution using a hash map. The idea is to traverse the array and use a hash map to keep track of the elements we have seen so far.


```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False
```


**Explanation:**
1. Create an empty dictionary `seen` to keep track of the count of each element.
2. Iterate through each element in `nums`.
3. For each element, check if it already exists in `seen` with a count of 1 or more.
4. If it does, return `True` (duplicate found).
5. If not, update the count of the element in `seen`.
6. If no duplicates are found after iterating through all elements, return `False`.


**Time Complexity:** (O(n)) because we traverse the list once.
**Space Complexity:** (O(n)) for storing elements in the hash map.


#### Set-Based Solution


Another efficient approach uses a hash set to keep track of the elements we've seen. This simplifies the logic by only checking for the existence of an element in the set.


```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```


**Explanation:**
1. Create an empty set `seen` to keep track of elements.
2. Iterate through each element in `nums`.
3. For each element, check if it already exists in `seen`.
4. If it does, return `True` (duplicate found).
5. If not, add the element to `seen`.
6. If no duplicates are found after iterating through all elements, return `False`.


**Time Complexity:** (O(n)) because we traverse the list once.
**Space Complexity:** (O(n)) for storing elements in the hash set.


### Problem 242: Valid Anagram


#### Problem Statement:
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.


**Example 1:**
- Input: `s = "anagram"`, `t = "nagaram"`
- Output: `true`


**Example 2:**
- Input: `s = "rat"`, `t = "car"`
- Output: `false`


**Constraints:**
- (1 leq text{s.length, t.length} leq 5 times 10^4)
- `s` and `t` consist of lowercase English letters.


#### Brute Force Solution (Using Sorting)


The simplest way to solve this problem is to sort both strings and compare them.


```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
```


**Explanation:**
1. Check if the lengths of `s` and `t` are equal. If not, return `False`.
2. Sort both strings.
3. Compare the sorted strings to check if they are equal.
4. If they are equal, return `True`; otherwise, return `False`.


**Time Complexity:** (O(n log n)) due to the sorting operation.
**Space Complexity:** (O(1)) as no extra space is used other than the input strings.


#### Optimized Solution (Using Hash Table)


A more efficient approach is to use a hash table to count the frequency of characters.


```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            if char_count.get(char, 0) == 0:
                return False
            char_count[char] -= 1
        return True
```


**Explanation:**
1. Check if the lengths of `s` and `t` are equal. If not, return `False`.
2. Create an empty dictionary `char_count` to store the frequency of characters in `s`.
3. Iterate through each character in `s` and update the frequency in `char_count`.
4. Iterate through each character in `t` and decrement the corresponding frequency in `char_count`.
5. If any character in `t` does not exist in `char_count` or its frequency becomes less than 0, return `False`.
6. If all frequencies match correctly, return `True`.


**Time Complexity:** (O(n)) because we traverse both strings once.
**Space Complexity:** (O(n)) for storing character frequencies.


### Problem 1: Two Sum

#### Problem Statement:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
- Input: `nums = [2, 7, 11, 15]`, `target = 9`
- Output: `[0, 1]`
- Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

**Example 2:**
- Input: `nums = [3, 2, 4]`, `target = 6`
- Output: `[1, 2]`

**Example 3:**
- Input: `nums = [3, 3]`, `target = 6`
- Output: `[0, 1]`

**Constraints:**
- \(2 \leq \text{nums.length} \leq 10^4\)
- \(-10^9 \leq \text{nums[i]} \leq 10^9\)
- \(-10^9 \leq \text{target} \leq 10^9\)
- Only one valid answer exists.

**Follow-up:** Can you come up with an algorithm that is less than \(O(n^2)\) time complexity?

### Brute Force Approach

The simplest way to solve this problem is by using a nested loop to check every possible pair of elements to see if they add up to the target.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

**Explanation:**
1. Loop through each element using index `i`.
2. For each element at index `i`, loop through the rest of the elements using index `j`.
3. Check if the sum of `nums[i]` and `nums[j]` is equal to the target.
4. If it is, return the indices `[i, j]`.

**Time Complexity:** \(O(n^2)\) due to the nested loops.
**Space Complexity:** \(O(1)\) as we are not using any extra space.

### Optimized Approach Using Hash Map

A more efficient approach is to use a hash map to keep track of the elements we have seen so far and their indices. This allows us to find the complement of the current element in constant time.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
```

**Explanation:**
1. Create an empty dictionary `num_to_index` to store the elements and their indices.
2. Iterate through each element in `nums` with its index `i`.
3. Calculate the complement of the current element (`complement = target - num`).
4. Check if the complement exists in `num_to_index`.
5. If it does, return the indices of the complement and the current element.
6. If it does not, add the current element and its index to `num_to_index`.

**Time Complexity:** \(O(n)\) because we traverse the list once and dictionary operations (insert and lookup) are \(O(1)\) on average.
**Space Complexity:** \(O(n)\) for storing elements in the hash map.

### Multiple Optimized Approaches

#### Two-Pass Hash Table

In this approach, we first store each element and its index in a hash table. In the second pass, we check if the complement exists in the hash table.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index and num_to_index[complement] != i:
                return [i, num_to_index[complement]]
```

**Explanation:**
1. Create a hash table `num_to_index` to store each element and its index.
2. In the second pass, iterate through each element and check if the complement exists in the hash table.
3. Ensure that the complement is not the same element by checking `num_to_index[complement] != i`.
4. Return the indices if a valid pair is found.

**Time Complexity:** \(O(n)\) because we have two separate passes through the list.
**Space Complexity:** \(O(n)\) for storing elements in the hash table.

#### Single-Pass Hash Table with Early Exit

Combining the insertion and lookup into a single pass allows us to find the solution more efficiently.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
```

**Explanation:**
1. Create an empty dictionary `num_to_index`.
2. Iterate through each element with its index.
3. Calculate the complement and check if it exists in the dictionary.
4. If it does, return the indices.
5. Otherwise, add the current element and its index to the dictionary.

**Time Complexity:** \(O(n)\)
**Space Complexity:** \(O(n)\)





