class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def pushs(self, val):
        self.items.append(val)

    def pops(self):
        if len(self.items) == 0:
            return "stack is empty"
        x = self.items.pop()
        return x

    def top(self):
        if len(self.items) == 0:
            return "no top, stack is empty"
        x = self.items[-1]
        return x

    def size(self):
        return len(self.items)


s = Stack()
s.pushs(1)
s.pushs(2)
s.pushs(3)
s.pushs(4)
s.pops()
s.top()

# stack implementation using queue

from collections import deque


class stack:
    def __init__(self):
        self.items = deque([])

    def push(self, val):
        self.items.append(val)
        for _ in range(len(self.items) - 1):
            self.items.append(self.items.popleft())

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items.popleft()

    def top(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[0]


lst = stack()
lst.push(100)
lst.push(200)
lst.push(300)
print(lst)
lst.pop()
print(lst)
lst.top()


# implement queue using stack

from collections import deque


class queue:
    def __init__(self):
        self.st1 = deque([])
        self.st2 = deque([])

    def push(self, val):
        if len(self.st1) != 0:
            for _ in range(len(stack)):
                self.st2.append(self.st1.pop())
        self.st1.append(val)
        for _ in range(len(self.st2)):
            self.st1.append(self.st1.pop())

    def pop(self):
        if len(self.st1) == 0:
            return "queue is empty"
        return self.st1.popleft()

    def top(self):
        if len(self.st1) == 0:
            return "queue"
        return self.st1[0]


lst = queue()
lst.push(100)
lst.push(200)
lst.push(300)
print(lst)
lst.pop()
print(lst)
lst.top()

# getmin in o(1) leetcode problem
from collections import deque


class stack:
    def __init__(self):
        self.items = deque([])

    def push(self, val):
        self.items.append(val)
        mini = min(self.items, self.pop, val)
        self.items.append(mini)

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items.popleft()

    def top(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[0]

    def getminimum(self):
        return self.items[len(self.items) - 1]


lst = stack()
lst.push(100)
lst.push(200)
lst.push(300)
print(lst)
lst.pop()
print(lst)
lst.top()
