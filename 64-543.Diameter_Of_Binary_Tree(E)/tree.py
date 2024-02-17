# Definition for a binary tree node.

from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    dia = 0

    def diameterOfBinaryTree(self, root: Optional[Node]) -> int:
        self.calc_diameter(root)
        return self.dia

    def calc_diameter(self, root):
        if not root:
            return 0
        left_tree = self.calc_diameter(root.left)
        right_tree = self.calc_diameter(root.right)
        self.dia = max(self.dia, (left_tree + right_tree))
        return max(left_tree, right_tree) + 1


root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
root_node.left.left = Node(4)
root_node.right.right = Node(5)
root_node.right = Node(3)
root_node.right.left = Node(6)
root_node.right.left.right = Node(7)
root_node.right.left.right.right = Node(8)
print(Solution().diameterOfBinaryTree(root_node))
