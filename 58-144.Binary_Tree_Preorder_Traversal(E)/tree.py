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

    # recursive pre-order
    def pre_order(self, root):
        if not root:
            return
        print(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)


class Solution:
    # iterative pre-order
    def preorderTraversal(self, root: Optional[Node]) -> List[int]:
        stack = [root]
        result = []
        while len(stack) > 0:
            element = stack.pop()
            result.append(element.val)
            if element and element.right:
                stack.append(element.right)
            if element and element.left:
                stack.append(element.left)
        return result


root_node = Node(3)
root_node.right = Node(1)
root_node.right.left = Node(2)
#
# root_node.left.left = Node(4)
# root_node.left.right = Node(5)
#
# root_node.right.left = Node(6)
# root_node.right.right = Node(7)

print(root_node)
print(Solution().preorderTraversal(root_node))
