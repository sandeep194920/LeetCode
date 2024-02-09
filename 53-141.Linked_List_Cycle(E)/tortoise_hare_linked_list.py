from typing import Optional


# DIRECTLY CODED ON LEET CODE AS IT IS HARD TO SET THIS UP IN HERE

# def print_ll(head, pos):
#     count = 0
#     temp = head
#     stop_node = None
#
#     while stop_node != temp:
#         print(temp.val)
#         if count == pos:
#             stop_node = temp
#         count += 1
#         temp = temp.next


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val}, {self.next})"


# def arr_to_ll(arr, pos):
#     if len(arr) == 0:
#         return None
#     head = ListNode(arr[0])
#     temp = head
#     pos_temp = head
#
#     for i in range(1, len(arr)):
#         temp.next = ListNode(arr[i])
#         temp = temp.next
#
#     for i in range(pos):
#         pos_temp = pos_temp.next
#
#     print('pos temp is', pos_temp)
#     temp.next = pos_temp
#     return head


# This solution is based on tortoise and hare algo, https://www.youtube.com/watch?v=354J83hX7RI&t=305s&ab_channel=takeUforward
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        if not fast:
            return False

        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if not fast:
                return False
            if slow == fast:
                return True

# my_head = arr_to_ll([3, 2, 0, -4], 1)
# result = Solution().hasCycle(my_head)
# print_ll(my_head, 1)
