from typing import Optional, List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[Node]:
        if len(inorder) == 0:
            return None

        root_val = preorder[0]
        root = Node(root_val)
        partition_index = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:partition_index + 1], inorder[:partition_index])
        root.right = self.buildTree(preorder[partition_index + 1:], inorder[partition_index + 1:])

        return root


root_node = Node(2)
root_node.left = Node(1)
root_node.right = Node(3)

# root_node.left.left = Node(3)
# root_node.right.left = Node(1)
# root_node.right.right = Node(5)

print(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
