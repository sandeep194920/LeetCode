# Definition for a binary tree node.

from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    dia = 0

    def isSameTree(self, p: Optional[Node], q: Optional[Node]) -> bool:
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True
        if p.val == q.val:
            left_comparison = self.isSameTree(p.left, q.left)
            right_comparison = self.isSameTree(p.right, q.right)
            return left_comparison and right_comparison
        else:
            return False


# TREE 1
root_node1 = Node(1)
root_node1.left = Node(2)
root_node1.right = Node(3)

# TREE 2
root_node2 = Node(1)
root_node2.left = Node(2)
root_node2.right = Node(3)

print(Solution().isSameTree(root_node1, root_node2))
