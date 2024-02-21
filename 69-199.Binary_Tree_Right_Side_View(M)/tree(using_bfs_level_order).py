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
        res, q = [], [root]

        if not root:
            return res

        while len(q) > 0:
            q_len = len(q)
            for i in range(q_len):
                el = q.pop(0)
                if i == q_len - 1:
                    res.append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
        return res

        # res, queue = [], []
        # if root:
        #     queue.append(root)
        # # append to add to queue, and pop(0) to remove
        # while len(queue) > 0:
        #     q_len = len(queue)
        #     sub_res = []
        #     for i in range(q_len):
        #         node = queue.pop(0)
        #         sub_res.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(sub_res)
        # return res


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
