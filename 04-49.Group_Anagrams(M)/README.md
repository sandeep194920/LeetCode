[Leetcode link](https://leetcode.com/problems/group-anagrams/)

```
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

- Note that we can do Bruteforce approach, but not doing it here
- Best approach is 26 alph key method - Time O(N) and space O(N)
  - Space o(N) in both approaches because we will have at max same number of keys as the original length of array
