from typing import Optional, List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    gn = 0

    def goodNodes(self, root: Node) -> int:
        gsf = root.val
        self.find_good_nodes(root, gsf)
        return self.gn

    def find_good_nodes(self, node, gsf):
        if not node:
            return None

        if node.val >= gsf:
            gsf = node.val
            self.gn += 1

        self.find_good_nodes(node.left, gsf)
        self.find_good_nodes(node.right, gsf)


root_node = Node(3)
root_node.left = Node(1)
root_node.right = Node(4)

root_node.left.left = Node(3)
root_node.right.left = Node(1)
root_node.right.right = Node(5)

print(Solution().goodNodes(root_node))
