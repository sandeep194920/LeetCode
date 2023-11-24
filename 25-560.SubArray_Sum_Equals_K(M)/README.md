[560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)

**Note:**
[Can't be solved for negative numbers as explained below and in this link](https://www.geeksforgeeks.org/longest-sub-array-sum-k/)

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 
```
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

```

```
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 
```

```
Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

```
**The sliding window solution doesn't work for negative numbers**
https://www.geeksforgeeks.org/longest-sub-array-sum-k/

Why? Let's say there is an array

```
[4, 1, 1, -2], k = 4 
```
Here, as soon as we increment j to index 1 we will find out that 
the sum is greater than k so we will start moving i pointer
forward which is wrong in this case. It is wrong because, 
when you add -2 keeping i at 0 (meaning i at index 0 and j at index 3), 
that would give us 4 which is equal to k. So it can't be solved using sliding window 
if negative numbers are present. Another approach we can use for this is
using hashmap (**To be continued**).