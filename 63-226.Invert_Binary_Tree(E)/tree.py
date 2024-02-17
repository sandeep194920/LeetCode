from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f'''Root-{self.val} L-{self.left} R-{self.right}'''
        if self.left:
            return f'''Root-{self.val} R-{self.left}'''
        if self.right:
            return f'''Root-{self.val} R-{self.right}'''
        return f'''Root-{self.val}'''


class Solution:
    def invertTree(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
root_node.left.left = Node(4)
root_node.right.right = Node(5)
root_node.right = Node(3)
root_node.right.left = Node(6)
root_node.right.left.right = Node(7)
root_node.right.left.right.right = Node(8)
print(root_node)
print(Solution().invertTree(root_node))
