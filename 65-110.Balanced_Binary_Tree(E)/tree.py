# Definition for a binary tree node.

from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diff = 0

    def isBalanced(self, root: Optional[Node]) -> bool:
        return self.check_balance(root)[0]

    def check_balance(self, root):
        if not root:
            return [True, 0]

        left = self.check_balance(root.left)
        right = self.check_balance(root.right)

        height = 1 + max(left[1], right[1])
        isBalanced = ((abs(left[1] - right[1]) <= 1) and left[0] and right[0])
        return [isBalanced, height]


root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
# root_node.left.left = Node(4)
# root_node.right.right = Node(5)
# root_node.right = Node(3)
# root_node.right.left = Node(6)
# root_node.right.left.right = Node(7)
# root_node.right.left.right.right = Node(8)
print(Solution().isBalanced(root_node))
