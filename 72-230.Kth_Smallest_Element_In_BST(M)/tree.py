from typing import Optional, List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def kthSmallest(self, root: Optional[Node], k: int) -> int:
        stack = []
        count = k
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                current_top = stack.pop()
                count -= 1
                if count == 0:
                    return current_top.val
                root = current_top.right


root_node = Node(2)
root_node.left = Node(1)
root_node.right = Node(3)

# root_node.left.left = Node(3)
# root_node.right.left = Node(1)
# root_node.right.right = Node(5)

print(Solution().kthSmallest(root_node, 2))
