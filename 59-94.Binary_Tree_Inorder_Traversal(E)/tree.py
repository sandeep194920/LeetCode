"""
Let's do In-order, Pre-Order and Post-Order traversal of tree here
https://youtu.be/jmy0LaGET1I?si=rHe0feN5U_gnoOan
"""
from typing import Optional, List


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left and self.right:
            return f'''Root-{self.val} L-{self.left} R-{self.right}'''
        return f'''Root-{self.val}'''


class Solution:
    # ITERATIVE APPROACH
    def inorderTraversal(self, root: Optional[Node]) -> List[int]:

        node = root
        res = []
        stack = []

        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

    # RECURSIVE APPROACH
    def inorderTraversalRecurse(self, root: Optional[Node]) -> List[int]:
        result = []
        self.inorder(result, root)
        return result

    def inorder(self, result, node):
        if not node:
            return
        self.inorder(result, node.left)
        result.append(node.val)
        self.inorder(result, node.right)


root_node = Node(1)
root_node.right = Node(2)
root_node.right.left = Node(3)
#
# root_node.left.left = Node(4)
# root_node.left.right = Node(5)
#
# root_node.right.left = Node(6)
# root_node.right.right = Node(7)

print(root_node)
print(Solution().inorderTraversalRecurse(root_node))
# print(Solution().inorderTraversal(root_node))
