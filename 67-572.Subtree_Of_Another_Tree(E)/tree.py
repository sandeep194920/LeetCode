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

    # THIS CODE DOESN'T WORK FOR EDGE CASE root1 = [1,1,null] and root2 = [1,null,null]

    # def isSubtree(self, root1: Optional[Node], root2: Optional[Node]) -> bool:
    #
    #     if not root1 and not root2:
    #         return True
    #
    #     if not root1 or not root2:
    #         return False
    #
    #     if root1.val != root2.val:
    #         left = self.isSubtree(root1.left, root2)
    #         right = self.isSubtree(root1.right, root2)
    #         return left or right
    #     else:
    #         left = self.isSubtree(root1.left, root2.left)
    #         right = self.isSubtree(root1.right, root2.right)
    #         return left and right

    def isSubtree(self, root: Optional[Node], subRoot: Optional[Node]) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right

    def isSameTree(self, root1: Optional[Node], root2: Optional[Node]):

        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        left = self.isSameTree(root1.left, root2.left)
        right = self.isSameTree(root1.right, root2.right)
        return left and right


# TREE 1
root_node1 = Node(3)
root_node1.left = Node(4)
root_node1.left.left = Node(1)
root_node1.left.right = Node(2)
root_node1.right = Node(5)

# TREE 2
root_node2 = Node(4)
root_node2.left = Node(1)
root_node2.right = Node(2)

# # TREE 1
# root_node1 = Node(1)
# root_node1.left = Node(1)
#
# # TREE 2
# root_node2 = Node(1)

print(Solution().isSubtree(root_node1, root_node2))
