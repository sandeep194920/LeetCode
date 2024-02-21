from typing import Optional, List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def isValidBST(self, root: Optional[Node]) -> bool:
        return self.isBST(root, float('-inf'), float('inf'))  # -infinity to +infinity

    def isBST(self, node, low, high):
        if not node:
            return True

        if not (node.val < high and node.val > low):
            return False

        left = self.isBST(node.left, low, node.val)
        right = self.isBST(node.right, node.val, high)
        return left == True and right == True


root_node = Node(2)
root_node.left = Node(1)
root_node.right = Node(3)

# root_node.left.left = Node(3)
# root_node.right.left = Node(1)
# root_node.right.right = Node(5)

print(Solution().isValidBST(root_node))
