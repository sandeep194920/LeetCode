128. Longest Consecutive Sequence
Medium
16.4K
692
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

**Example 1:**
```shell
Input: nums = [100,4,200,1,3,2]
Output: 4
```

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


**Example 2:**

```shell
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```


##### APPROACH Using a SET (Look up (checking if element exists) in SET is O(N)) 

First visualize the pattern yourself. The human visualization can get this pattern on a number line by
looking at the elements

  1 2 3 4       100            200
Length is 4   Length is 1   Length is 1

By visualizing this, we know that, for a pattern to start at a particular number, it should not have a left
neighbour

For example, pattern starts at 1 (that doesn't have left neighbour)
Similarly pattern starts at 100 (that doesn't have left nbr)
Similarly pattern starts at 200 (that doesn't have left nbr)

So now we have 3 patterns. Basically, at every element we check if it is a pattern starting by checking if
it doesn't have a left nbr. IF no left nbr then pattern starts. Once we found that an element is a start of
the pattern, we then see how long the pattern goes by checking the right neighbours. If we don't find a right
nbr we stop and note down the length of that pattern and update the max_length

If an element do have a left nbr, we just skip and continue to next element

NOTE : To check if the element (nbr element) exists in a list, it is O(N), so it is better we convert input list
into SET to it will be O(1)
