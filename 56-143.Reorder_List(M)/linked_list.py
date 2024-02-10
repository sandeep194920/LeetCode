from typing import Optional


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def arr_to_ll(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    temp = head

    for i in range(1, len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next

    return head


def print_ll(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> ListNode:
        """
        Do not return anything, modify head in-place instead.
        """

        left = head
        slow, fast = head, head

        if not left or not left.next or not left.next.next:
            return head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 1 2 3 4                 5< 6 < P7

        # 1 > 2 > 3 > 4 < 5 < 6 < 7

        # 1 > 2 > 3 >
        #               4
        # 7 > 6 > 5 >

        # 1 > 2 > 3 > 4 < 5 < 6 < 7

        cur = slow.next
        pre = None

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        right = pre
        slow.next.next = slow
        slow.next = None

        # reordering
        cl = left
        cr = right

        while cl and cr:
            cl = cl.next
            cr = cr.next
            left.next = right
            right.next = cl
            left = cl
            right = cr
        return head


my_head = arr_to_ll([1, 2, 3, 4, 5])
# print_ll(my_head)
result = Solution().reorderList(my_head)
print_ll(result)
