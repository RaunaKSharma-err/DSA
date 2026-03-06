class node:
    def __init__(self, val):
        self.val = val
        self.next = None


class singlyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        newNode = node(val)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newNode

    def insert(self, val, pos):
        newNode = node(val)
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            curr = self.head
            prev = None
            count = 0
            while count < pos and curr is not None:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = newNode
            newNode.next = curr

    def deleteOnPosition(self, pos):
        if self.head == None:
            print("linkedlist is empty")
        elif pos == 0:
            curr = self.head
            self.head = curr.next.next
        else:
            curr = self.head
            count = 1
            while curr is not None and count < pos:
                curr = curr.next
                count += 1
            curr.next = curr.next.next

    def deleteVal(self, val):
        if self.head == None:
            print("linkedlist is empty")
        else:
            curr = self.head
            while curr is not None:
                if curr.val == val:
                    prev.next = curr.next
                    found = True
                    break
                prev = curr
                curr = curr.next
            if found == False:
                print("value not found in the linkedlist")

    def traverse(self):
        if self.head == None:
            print("linkedlist is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val)
                curr = curr.next

    def middleNode(self):
        fast = self.head
        slow = self.head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow.val


obj = singlyLinkedList()
obj.append(3)
obj.append(4)
obj.append(5)
obj.append(6)
a = obj.middleNode()
obj.traverse()
print(a)
