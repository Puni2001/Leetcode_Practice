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





