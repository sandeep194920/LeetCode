class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"({self.data}, {self.next})"


def arr_to_ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    temp = head

    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next

    return head


def print_ll(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next


def reverse_list(head: Node) -> Node:
    cur = head
    prev = None

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def addOne(head: Node) -> Node:
    # 4-> 5-> 9
    # 0  1  1
    # 4  6  0

    # 9 -> 5 -> 4
    # 1   C    C
    # T<- TH<-TH

    # 0   6   4

    temp = head
    # total = (temp.data + 1) % 10
    # carry = int(temp.data / 10)
    carry = 1
    total_head = None
    while temp:
        total = (temp.data + carry) % 10
        carry = int((temp.data + carry) / 10)
        total_node = Node(total)
        total_node.next = total_head
        total_head = total_node
        temp = temp.next

    if carry > 0:
        total_node = Node(carry)
        total_node.next = total_head
        total_head = total_node
    return total_head


my_head = arr_to_ll([1, 5, 2])
# print(reverse_list(my_head))
print_ll(addOne(reverse_list(my_head)))
