[Leetcode link](https://leetcode.com/problems/top-k-frequent-elements/)

```
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
```

Bucket sort Approach

```
- Create a frequency mapping of elements - {each element : times repeated}
- Create an array of length - number of elements + 1.
    - Loop over frequency map and fill the array.

Example:
Original array - [a a a a b b b b b c d e e]

freq_map = {
    a:4,
    b:5,
    c:1,
    d:1,
    e:2
}
    [c,d]                  [a]   [b]
__    __    __     __      __     __     __    __    __    __    __    __    __    __
0      1     2      3       4      5      6     7     8     9    10    11    12    13
```

#### Why do we need 13 index here.

- The array length is 13 so we also need index 13 and not just 12.
- Yes, 0 - 12 would be 13 but 0 is not being used really here. 0 means, number of elements repeated 0 times and we don't add anything to that bucket
- Let's say if we have an array that looks like this `[b,b,b,b,b,b,b,b,b,b,b,b,b]` (b repeated 13 times), then we add b to 13th dash here like this

```
                                                                                   [b]
__    __    __     __      __     __     __    __    __    __    __    __    __    __
0      1     2      3       4      5      6     7     8     9    10    11    12    13
```

- Then we need to traverse from right side of this array and return k frequent elements.
- So above, b, and a are frequently repeated elements, so we return [b,a]

APPROCAH 2

[https://leetcode.com/problems/top-k-frequent-elements/solutions/669782/javascript-no-sorting-o-n-time/?q=javascript&orderBy=most_votes](Using JS MAP)
