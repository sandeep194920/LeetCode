[Leetcode link](https://leetcode.com/problems/product-of-array-except-self/)

```
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Follow up: Can you solve the problem in O(1) 
extra space complexity? (The output array does not count as extra space 
for space complexity analysis.)
```

**Approach 1**

Let's first solve this using bruteforce. 
The problem with this approach is, for large inputs we get "Time limit exceeded"

**Approach 2**

Then we will solve efficiently. First we will pass from left end to right end. 
We will have a product, p initialized to 1, and during the traverse at each element, 
we will multiply this p excluding this element.

  input -> p=1  [1, 2, 3, 4]
  
  left pass ->  [A, B, C, D] -> At position A, the products of all previous
  
elements not including 1 is p which is 1. So once we traverse all from left to right
this is what the array looks

At 1st element  -> [1] P = 1
At 2nd element  -> [P=1, 1] -> P = 1 -> the second 1 here is the very first element of input  
At 3rd element  -> [1, 1, 2] -> P = 2 the 3rd element 2 is the multiplication of previous elements tracked in p at each point 
At 4th element  -> [1, 1, 2, 6] 


Similarly, we will do it from right to left pass and put it in a separate array.
Then we can multiply both left and right arrays. 

Once you get comfortable, we can do it all in one array. Right to left pass 
will be done a bit differently where we can multiply to same element once we know
the output.
