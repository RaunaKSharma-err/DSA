// LL: Has Loop ( ** Interview Question)

// Instructions

// Write a method called hasLoop that is part of the linked list class.
// The method should be able to detect if there is a cycle or loop present in the linked list.
// You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.
// This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a loop in the linked list, the two pointers will eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.

// The method should follow these guidelines:

// Create two pointers, slow and fast, both initially pointing to the head of the linked list.
// Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.
// If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return true.
// If the fast pointer reaches the end of the list or encounters a null value, it means there is no loop in the list. In this case, the method should return false.

// Output:
// Return true if the linked list has a loop.
// Return false if the linked list does not have a loop.

// Constraints:
// You are not allowed to use any additional data structures (such as arrays) or modify the existing data structure.
// You can only traverse the linked list once.

// Method signature:
// public boolean hasLoop()

//SOLUTION

// In this solution what we will see that if the two of the pointers meet at a same node and if they meets then there is a cycle in the linkedlist

class HasLoop {
    private Node head;
    private Node tail;
    private int length;

    class Node {
        int value;
        Node next;

        public Node(int value) {
            this.value = value;
        }
    }

    public HasLoop(int value) {
        Node newNode = new Node(value);
        head = newNode;
        tail = newNode;
        length = 1;
    }

    public void append(int value) {
        Node newnNode = new Node(value);
        if (length == 0) {
            head = newnNode;
            tail = newnNode;
        }
        tail.next = newnNode;
        tail = newnNode;
        newnNode.next = head;
        length++;
    }

    public void print() {
        Node temp = head;
        if (temp == null) {
            System.out.println("LinkedList is empty");
        }
        for (int i = 0; i < length; i++) {
            System.out.println("");
            System.out.println(temp.value);
            temp = temp.next;
        }
    }

    public boolean HasLoopFunction() {
        Node fast = head;
        Node slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                System.out.println("Cycle found");
                return true;
            }
        }
        System.out.println("Cycle not found");
        return false;
    }

    public static void main(String[] args) {
        HasLoop ll = new HasLoop(1);
        ll.append(2);
        ll.append(3);
        ll.append(4);
        ll.print();
        ll.HasLoopFunction();
    }
}