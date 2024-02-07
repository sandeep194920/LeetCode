from typing import Optional


def print_ll(head):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next


def arr_to_ll(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    temp = head

    for i in range(1, len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next

    return head


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val}, {self.next})"


## LEETCODE SOLUTION BELOW

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)  # the value can be anything
        t = dummy
        t1, t2 = list1, list2

        while t1 or t2:
            if t1 and (not t2 or t1.val <= t2.val):
                t.next = t1
                t = t1  # or t = t.next
                t1 = t1.next
            else:
                t.next = t2
                t = t2  # or t = t.next
                t2 = t2.next
        return dummy.next


# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

list1 = [1]
list2 = []

h1 = arr_to_ll(list1)
h2 = arr_to_ll(list2)
result = Solution().mergeTwoLists(h1, h2)
print_ll(h1)
