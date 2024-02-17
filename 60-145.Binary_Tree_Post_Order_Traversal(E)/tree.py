from typing import Optional, List


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    # def __repr__(self):
    #     if self.left and self.right:
    #         return f'''Root-{self.val} L-{self.left} R-{self.right}'''
    #     return f'''Root-{self.val}'''
    def __repr__(self):
        return f'{self.val}'


class Solution:
    # RECURSIVE
    def postorderTraversalRecursive(self, root: Optional[Node]) -> List[int]:
        result = []
        self.post_order_rec(root, result)
        return result

    def post_order_rec(self, node: Optional[Node], result):
        if not node:
            return
        self.post_order_rec(node.left, result)
        self.post_order_rec(node.right, result)
        result.append(node.val)

    # RECURSIVE
    def postorderTraversalIterative(self, root: Optional[Node]) -> List[int]:
        stack1, stack2, result = [root], [], []
        while len(stack1) > 0:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while len(stack2) > 0:
            result.append(stack2.pop().val)
        return result


root_node = Node(1)
root_node.left = Node(2)
root_node.left.left = Node(4)
root_node.left.right = Node(5)

root_node.right = Node(3)
root_node.right.left = Node(6)
root_node.right.left.right = Node(7)
root_node.right.left.right.right = Node(8)

#
# root_node.left.left = Node(4)
# root_node.left.right = Node(5)
#
# root_node.right.left = Node(6)
# root_node.right.right = Node(7)

# print(root_node)
# print(Solution().postorderTraversalRecursive(root_node))
print(Solution().postorderTraversalIterative(root_node))
# print(Solution().inorderTraversal(root_node))
