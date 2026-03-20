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

    def removeOccurance(self, n):
        curr = self.head
        while curr:
            if n == curr.val and curr == self.head:
                self.head = curr.next
            elif n == curr.val:
                if curr.next is None:
                    curr = curr.prev
                    curr.next.prev = None
                    curr.next = None
                else:
                    temp = curr.prev
                    temp.next = curr.next
                    curr.next.prev = temp
            curr = curr.next


dll1 = solution()
dll1.append(9)
dll1.append(9)
dll1.append(9)
dll1.append(9)
dll1.append(9)
dll1.append(9)
dll1.append(9)
dll1.traverse()

dll2 = solution()
dll2.append(9)
dll2.append(9)
dll2.append(9)
dll2.append(9)
dll2.traverse()


def addTwoNumbers(l1, l2):
    dummy = node(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = node(total % 10)
        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next


a = addTwoNumbers(dll1.head, dll2.head)
