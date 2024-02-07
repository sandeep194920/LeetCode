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


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        odd, even = head, head.next
        temp_odd, temp_even = odd, even

        while temp_odd.next and temp_even.next:
            temp_odd.next = temp_even.next
            temp_odd = temp_odd.next
            temp_even.next = temp_odd.next
            temp_even = temp_even.next
        temp_odd.next = even
        return head


head = [1, 2, 3, 4, 5]
head = []
head = arr_to_ll(head)
print(head)
result = Solution().oddEvenList(head)
print_ll(result)
