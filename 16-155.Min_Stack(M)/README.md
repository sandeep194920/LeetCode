[155. Min Stack](https://leetcode.com/problems/min-stack/)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
```
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

Output
```
[null,null,null,null,-3,null,0,-2]
```

Explanation

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

### Approach 1

We can use two stacks, one for normal stack where we push each element on to it and pop from it. We also create a second stack just to hold the minimum value. Whatever value is pushed then we compare that with current minimum and then place them properly in current positions of min stack.  

### Approach 2

Same as above approach, but instead of using two different stacks we can use a single stack and store a tuple or sub array at every point. In that sub array, the first element is the stack element and 2nd element is the minimum element upto that point.