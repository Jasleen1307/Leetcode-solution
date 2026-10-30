
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # Get value at a given index
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for i in range(index):
            curr = curr.next

        return curr.val

    # Add node at head
    def addAtHead(self, val):
        newNode = Node(val)

        newNode.next = self.head
        self.head = newNode

        self.size += 1

    # Add node at tail
    def addAtTail(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
        else:
            curr = self.head

            while curr.next is not None:
                curr = curr.next

            curr.next = newNode

        self.size += 1

    # Add node at a given index
    def addAtIndex(self, index, val):
        if index < 0:
            index = 0

        if index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        newNode = Node(val)
        curr = self.head

        for i in range(index - 1):
            curr = curr.next

        newNode.next = curr.next
        curr.next = newNode

        self.size += 1

    # Delete node at a given index
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head

            for i in range(index - 1):
                curr = curr.next

            curr.next = curr.next.next

        self.size -= 1
