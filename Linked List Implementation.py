class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        #if the linked list is empty we create a new node and add it at head
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            #insertion time of o(1)
            self.tail.next = newNode
            self.tail = newNode

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.print()