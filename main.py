class node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class solution:
    def __init__(self):
        self.head = None

    def append(self, val):
        newNode = node(val)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            newNode.prev = curr

    def insertAtHead(self, val):
        if self.head == None:
            newNode = node(val)
            self.head = newNode
        else:
            curr = self.head
            newNode = node(val)
            self.head = newNode
            newNode.next = curr
            curr.prev = newNode

    def traverse(self):
        curr = self.head
        print("nodes :")
        while curr:
            print(curr.val)
            curr = curr.next

    def insertAt(self, val, n):
        newNode = node(val)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            while n > 1 and curr.next:
                curr = curr.next
                n -= 1
            temp = curr.prev
            temp.next = newNode
            newNode.next = curr
            curr.prev = newNode

    def reverseDLinkedList(self):
        curr = self.head
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev


dll = solution()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
dll.traverse()
dll.reverseDLinkedList()
dll.traverse()
