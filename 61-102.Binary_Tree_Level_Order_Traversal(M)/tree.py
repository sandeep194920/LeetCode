from typing import Optional, List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        res, queue = [], []
        if root:
            queue.append(root)
        # append to add to queue, and pop(0) to remove
        while len(queue) > 0:
            q_len = len(queue)
            sub_res = []
            for i in range(q_len):
                node = queue.pop(0)
                sub_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sub_res)
        return res


root_node = Node(1)
root_node.left = Node(2)
root_node.right = Node(3)
root_node.left.left = Node(4)
root_node.right.right = Node(5)
root_node.right = Node(3)
root_node.right.left = Node(6)
root_node.right.left.right = Node(7)
root_node.right.left.right.right = Node(8)
print(Solution().levelOrder(root_node))
