# Definition for a binary tree node.

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
    def lowestCommonAncestor(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        if p.val == root.val or q.val == root.val:
            return root

        if ((p.val < root.val) and (q.val > root.val) or
                (q.val < root.val) and (p.val > root.val)):
            return root

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)


# [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8

root_node = Node(6)
root_node.left = Node(2)
root_node.right = Node(8)

root_node.left.left = Node(0)
root_node.left.right = Node(4)

root_node.right.left = Node(7)
root_node.right.right = Node(9)

root_node.left.right.left = Node(3)
root_node.left.right.right = Node(5)

# p = 2, q = 8 -> output = 6
# p_node = root_node.left
# q_node = root_node.right

# p = 7, q = 9 -> output = 8
p_node = root_node.right.left
q_node = root_node.right.right

print(Solution().lowestCommonAncestor(root_node, p=p_node, q=q_node).val)
