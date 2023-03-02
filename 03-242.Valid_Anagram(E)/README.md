[Leetcode link](https://leetcode.com/problems/valid-anagram/)

```
242. Valid Anagram


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true


Example 2:

Input: s = "rat", t = "car"
Output: false
```

- Make one hashmap for each string - so two in total
- Compare both the hashmaps. If same then true else false
