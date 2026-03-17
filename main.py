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


l1 = solution()
l1.append(1)
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(3)
l1.append(4)
l1.traverse()
