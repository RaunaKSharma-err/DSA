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

    def traverse(self, n):
        if n == None:
            print("linkedlist is empty")
        else:
            curr = n
            print("nodes:")
            while curr is not None:
                print(curr.val)
                curr = curr.next

    def circularLinkedList(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = self.head.next

    def middleNode(self):
        fast = self.head
        slow = self.head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow.val

    def reverseLinkedList(self):
        curr = self.head
        prev = None
        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        self.head = prev

    def detectCycleInLinkedList(self):
        fast = self.head
        slow = fast
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

    def detectCycleLength(self):
        fast = self.head
        slow = fast
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                count = 0
                while fast.next != slow:
                    fast = fast.next
                    count += 1
                return count
        return None

    def oddEvenLinkedList(self):
        if self.head is None or self.head.next is None:
            return self.head
        odd = self.head
        even = self.head.next
        evenHead = even
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return self.head

    def removeNthNode(self, n):
        slow = self.head
        fast = self.head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return self.head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head

    def removeDuplicates(self):
        curr = self.head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return self.head

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


l1 = singlyLinkedList()
l1.append(1)
l1.append(2)
l1.append(4)
# l1.traverse()
l2 = singlyLinkedList()
l2.append(1)
l2.append(3)
l2.append(4)
l2.append(4)
l2.append(5)
l2.append(6)
# l2.traverse()


def mergeLinkedList(l1, l2):
    dummy = node(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next


a = mergeLinkedList(l1.head, l2.head)
l2.traverse(a)
