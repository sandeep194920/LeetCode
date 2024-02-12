from typing import Optional

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        temp = head
        store = {None: None}

        while temp:
            store[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        new_head = store[head]
        copy_temp = new_head

        while temp:
            copy_temp.next = store[temp.next]
            copy_temp.random = store[temp.random]
            temp = temp.next
            copy_temp = copy_temp.next

        return new_head
