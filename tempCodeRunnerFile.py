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
