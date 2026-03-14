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


obj = solution()
obj.append(1)
obj.append(2)
obj.append(3)
obj.insertAtHead(0)
obj.insertAt(9, 2)
obj.traverse()


def checkParanthesis(string: str):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for i in string:
        if i in "({[":
            stack.append(i)
        elif i in ")}]":
            if not stack or stack[-1] != pairs[i]:
                return False
        return len(stack) == 0


a = checkParanthesis("([)]")
print(a)
