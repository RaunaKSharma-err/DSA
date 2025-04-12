// Find Middle Node ( ** Interview Question)

// Instructions
// Implement a method called findMiddleNode that returns the middle node of the
// linked list.
// If the list has an even number of nodes, the method should return the second
// middle node.

// Note: this LinkedList implementation does not have a length member variable.

// Method signature:
// public Node findMiddleNode()

// Example:
// LinkedList myList = new LinkedList(1);
// myList.append(2);
// myList.append(3);
// myList.append(4);
// myList.append(5);
// Node middleNode = myList.findMiddleNode();
// System.out.println(middleNode.value); // Output: 3

// myList.append(6);
// middleNode = myList.findMiddleNode();
// System.out.println(middleNode.value); // Output: 4

// When the linked list has an odd number of nodes, like 1 -> 2 -> 3 -> 4 -> 5,
// the function will find
// the exact middle node. In this case, it will return the node containing the
// value 3.
// When the linked list has an even number of nodes, there will be two middle
// nodes. The findMiddleNode
// function will return the second of these two middle nodes.
// For example, if the linked list is 1 -> 2 -> 3 -> 4 -> 5 -> 6, the two middle
// nodes are 3 and 4.
// The function will return the node containing the value 4.

// SOLUTION

public class findMiddleNode {

    private Node head;
    private Node tail;

    class Node {
        int value;
        Node next;

        public Node(int value) {
            this.value = value;
        }
    }

    public findMiddleNode(int value) {
        Node newNode = new Node(value);
        head = newNode;
        tail = newNode;
    }

    public void append(int value) {
        Node newnNode = new Node(value);
        if (head == null) {
            head = newnNode;
            tail = newnNode;
        } else {
            tail.next = newnNode;
            tail = newnNode;
        }

    }

    public void print() {
        Node temp = head;
        while (temp != null) {
            System.out.println("");
            System.out.println("value: " + temp.value);
            temp = temp.next;
        }
    }

    public Node MiddleNodeFunction() {
        Node slow = head;
        Node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public static void main(String[] args) {
        findMiddleNode ll = new findMiddleNode(4);
        ll.append(5);
        ll.append(8);
        ll.append(50);
        ll.append(10);
        ll.print();
        System.out.println("Middle value is :" + ll.MiddleNodeFunction().value);

    }
}