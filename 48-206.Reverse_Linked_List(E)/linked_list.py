# When we need to create a new node, we call this
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def reverse_using_pointers(self):

        prev_node = None
        curr_node = self.head
        next_node = curr_node.next
        #   10 20 30 40
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        temp = self.head
        self.head = self.tail
        self.tail = temp

        return self

    def reverse_recursively(self, head: Node):

        # REMEMBER - In base case you return not just the last node but also making that node as new HEAD.
        # you need to return the same new head in all the recursive calls above the call stack

        if not head or not head.next:
            return head  # note as i explained above, we are making this
            # last node as new head and return that in all other cases until first node

        new_head = self.reverse_recursively(head.next)

        # head is still the current head (pointing to the current element which is not yet reversed)
        head.next.next = head
        head.next = None

        self.head = new_head
        return new_head  # note as i explained above, we are making this
        # last node as new head and return that in all other cases until first node


my_linked_list = LinkedList(10)
my_linked_list.push(20)
my_linked_list.push(30)
my_linked_list.push(40)
# my_linked_list.reverse_using_pointers()
my_linked_list.print()
print('''''''''''')
my_linked_list.reverse_recursively(my_linked_list.head)

my_linked_list.print()
