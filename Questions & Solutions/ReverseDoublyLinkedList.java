// DLL: Reverse ( ** Interview Question)
// Instructions
// Implement a method called reverse() that reverses the order of the nodes in
// the list.

// This method should reverse the order of the nodes in the list by manipulating
// the pointers of each node, not by swapping the values within the nodes.

// Method Signature:

// public void reverse()

// Output:

// No explicit output is returned. However, the method should modify the doubly
// linked list such that the order of the nodes is reversed.

// Constraints:

// The doubly linked list may be empty or have one or more nodes.

// Example:

// Consider the following doubly linked list:

// Head: 1
// Tail: 5
// Length: 5

// Doubly Linked List:
// 1 <-> 2 <-> 3 <-> 4 <-> 5

// After calling reverse(), the list should be:

// Head: 5
// Tail: 1
// Length: 5

// Doubly Linked List:
// 5 <-> 4 <-> 3 <-> 2 <-> 1

public class ReverseDoublyLinkedList {
    private Node head;
    private Node tail;
    private int length;

    class Node {
        Node prev;
        Node next;
        int value;

        public Node(int value) {
            this.value = value;
        }
    }

    public ReverseDoublyLinkedList(int value) {
        Node newNode = new Node(value);
        head = newNode;
        tail = newNode;
        length++;
    }

    public void append(int value) {
        Node newNode = new Node(value);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        length++;
    }

    public void print() {
        if (length == 0) {
            System.out.println("Double LinkedList is Empty ...");
        } else {
            Node temp = head;
            System.out.println("");
            while (temp != null) {
                System.out.println(temp.value);
                temp = temp.next;
            }
        }
    }

    public void ReverseDoublyLinkedListFunction() {
        Node temp = head;
        head = tail;
        tail = temp;
        
    }

    public static void main(String[] args) {
        ReverseDoublyLinkedList dll = new ReverseDoublyLinkedList(1);
        dll.append(2);
        dll.append(3);
        dll.append(4);
        dll.print();
    }
}
