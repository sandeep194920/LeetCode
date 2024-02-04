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

    def pop(self):
        if not self.head:
            return None

        # this code is written below in else loop (edge case)
        # if self.length == 1:
        #     self.head = None
        #     self.tail = None
        #     return temp

        else:
            temp = self.head
            prev = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
            self.length -= 1
            # edge case if we have one single node
            if self.length == 0:
                self.head = None
                self.tail = None

        return temp.value

    def unshift(self, value):
        # inserting a new node at the beginning
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def shift(self):
        # remove node at the start
        if not self.head:
            return None
        node = self.head
        self.head = self.head.next
        node.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return node

    def get(self, index):
        if index < 0 or index >= self.length:
            return -1

        temp = self.head
        i = 0
        while i < index:
            temp = temp.next
            i += 1
        return temp.value

    def set(self, index, value):
        if index < 0 or index >= self.length:
            return -1

        i = 0
        temp = self.head
        while i < index:
            temp = temp.next
            i += 1
        temp.value = value
        return self

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return -1

        new_node = Node(value)

        if index == 0:
            return self.unshift(value)

        # 10 20 -> 30 40
        #     -> 60 ->
        temp = self.head
        i = 0
        while i < index - 1:
            temp = temp.next
            i += 1
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return self

    def remove(self, index):
        if index == 0:
            return self.shift()
        elif index < 0 or index >= self.length:
            return -1
        else:
            # 10 20 40 50
            temp = self.head
            prev = self.head
            i = 0

            while i < index:
                prev = temp
                temp = temp.next
                i += 1
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return self

    def reverse(self):

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


my_linked_list = LinkedList(10)
my_linked_list.push(20)
my_linked_list.push(30)
my_linked_list.push(40)
my_linked_list.reverse()
my_linked_list.print()
