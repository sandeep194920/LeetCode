# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:

        # first element in the stack - [current_value, current_minimum_value]
        if len(self.stack) == 0:
            self.stack.append([val, val])

        # from second element onwards
        else:
            current_min = self.stack[-1][1]
            current_min = min(current_min, val)
            self.stack.append([val, current_min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # return -3
minStack.pop()
print(minStack.top())  # return 0
print(minStack.getMin())  # return -2
