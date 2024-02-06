# Converting array to LL format
from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val}, {self.next})"


class LinkedList:

    def print_ll(self, head):
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next

    def arr_to_ll(self, arr):
        head = ListNode(arr[0])
        temp = head

        for i in range(1, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next

        return head


# Submit the below to leetcode
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2 = l1, l2
        dummy = ListNode(0)
        temp = dummy
        carry_val = 0

        while t1 or t2 or carry_val > 0:
            if t1:
                t1_val = t1.val
                t1 = t1.next
            else:
                t1_val = 0
            if t2:
                t2_val = t2.val
                t2 = t2.next
            else:
                t2_val = 0
            total = (t1_val + t2_val + carry_val) % 10
            carry_val = int((t1_val + t2_val + carry_val) / 10)
            temp.next = ListNode(total)
            temp = temp.next
        return dummy.next


n1 = [2, 4, 3]
n2 = [5, 6, 4]

h1 = LinkedList().arr_to_ll(n1)
h2 = LinkedList().arr_to_ll(n2)

res = Solution().addTwoNumbers(h1, h2)
LinkedList().print_ll(res)
