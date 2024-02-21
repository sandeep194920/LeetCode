from typing import Optional, List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def rightSideView(self, root: Optional[Node]) -> List[int]:
        res, stack = [], []
        self.reverse_pre_order(root, 0, res, stack)
        return res

    def reverse_pre_order(self, node, level, res, stack) -> Optional[List[int]]:
        if not node:
            return
        if len(stack) == level:
            stack.append(node)
            res.append(node.val)

        self.reverse_pre_order(node.right, level + 1, res, stack)
        self.reverse_pre_order(node.left, level + 1, res, stack)


# TEST SET 1
# root_node = Node(1)
# root_node.left = Node(2)
# root_node.right = Node(3)


# TEST SET 2
root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
root_node.left.right = Node(5)
root_node.right.right = Node(4)

# TEST SET 3
# root_node = Node(1)
# root_node.right = Node(3)

# TEST SET 4
# root_node = None
# root_node.right = Node(3)

print(Solution().rightSideView(root_node))
