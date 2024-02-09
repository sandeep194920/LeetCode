from typing import Optional


def print_ll(head):
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val}, {self.next})"


def arr_to_ll(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    temp = head

    for i in range(1, len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next

    return head


# SUBMIT BELOW CODE FOR LEETCODE
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = n
        fast, slow = head, head

        while count != 0:
            if not fast:  # Edge case if n is more than given nodes
                return None
            fast = fast.next
            count -= 1

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next
        slow.next = slow.next.next
        temp.next = None
        return head


my_head = arr_to_ll([1, 2, 3, 4, 5])
# my_head = arr_to_ll([1])  # Edge case, n = 1, output is None.
# my_head = arr_to_ll([1, 2])  # Edge case, n = 2. Output is 2 (head needs to be removed, so we need to return head.next

result = Solution().removeNthFromEnd(my_head, n=1)

print_ll(my_head)
