from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val}, {self.next})"


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


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if not head.next:
            return True
        # At this point, slow should be at the middle of linked list
        # let's now reverse the second half of the list (which starts with slow.next)

        current = slow.next
        head_2 = current
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # now previous points to the end of the linked list
        # which technically should be our starting point of second half of list
        slow.next = None
        head_2.next = slow

        # At this point we will have like this     1 -> 2 -> 3 <- 2 <- 1

        # So we will place two pointers one each at start and end
        # start is pointed by head and end is pointed by previous

        start = head
        end = prev
        print(start.val, end.val)

        while start and end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        return True


my_head = arr_to_ll([1, 1, 2, 1])
# my_head = arr_to_ll([1, 2, 3, 4, 2, 1])

result = Solution().isPalindrome(my_head)

# print_ll(result)
print(result)
