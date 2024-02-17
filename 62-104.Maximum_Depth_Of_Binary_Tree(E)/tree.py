# Definition for a binary tree node.
from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    # Using Recursion
    def maxDepthRecr(self, root: Optional[Node]) -> int:
        node = root
        if not node:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

    # Using LevelOrder
    def maxDepthIter(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        q, height = [root], 0
        while len(q) > 0:
            level = len(q)
            height += 1
            for i in range(level):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return height


root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
root_node.left.left = Node(4)
root_node.right.right = Node(5)
#
# root_node.right = Node(3)
# root_node.right.left = Node(6)
# root_node.right.left.right = Node(7)
# root_node.right.left.right.right = Node(8)
print(Solution().maxDepthIter(root_node))
