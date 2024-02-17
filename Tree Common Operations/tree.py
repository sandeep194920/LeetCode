"""
Let's do In-order, Pre-Order and Post-Order traversal of tree here
https://youtu.be/jmy0LaGET1I?si=rHe0feN5U_gnoOan
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left and self.right:
            return f'''Root-{self.val} L-{self.left} R-{self.right}'''
        return f'''Root-{self.val}'''

    def pre_order(self, root):
        if not root:
            return
        print(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val)

    def level_order(self, root):
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
#
# root_node.left.left = Node(4)
# root_node.left.right = Node(5)
#
# root_node.right.left = Node(6)
# root_node.right.right = Node(7)

print(root_node)
print(root_node.level_order(root_node))
