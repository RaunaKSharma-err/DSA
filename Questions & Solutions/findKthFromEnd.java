// LL: Find Kth Node From End ( ** Interview Question)

// Instructions
// Implement a method called findKthFromEnd that returns the k-th node from the end of the list.
// If the list has fewer than k nodes, the method should return null.

// Note: This implementation of the Linked List class does not have the length attribute.

// Method signature:
// public Node findKthFromEnd(int k)

// Example:
// LinkedList myList = new LinkedList(1);
// myList.append(2);
// myList.append(3);
// myList.append(4);
// myList.append(5);
// Node result = myList.findKthFromEnd(2); // Output: Node with value 4

// result = myList.findKthFromEnd(5); // Output: Node with value 1
// result = myList.findKthFromEnd(6); // Output: null

// Note:
// In this problem, you should use the two-pointer technique to efficiently find the k-th node from
// the end of the linked list.

//SOLUTION

// what we are doing in this solution is we are moving the first pointer towards the required node like
//  if the (kth) node is 2 then we do move the second pointer 2 node front and then we move both the
//  pointer until the pointer at the last gets null.    

public class findKthFromEnd {
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

    public findKthFromEnd(int value) {
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
        length++;
    }

    public void print() {
        Node temp = head;
        if (temp == null) {
            System.out.println("LinkedList is empty");
        }
        System.out.println("");
        for (int i = 0; i < length; i++) {
            System.out.println(temp.value);
            temp = temp.next;
        }
    }

    public Node findKthFromEndFunction(int k) {
        Node fast = head;
        Node slow = head;

        for (int i = 0; i < k; i++) {
            if (fast == null)
                return null;
            fast = fast.next;
        }
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow;

    }

    public static void main(String[] args) {
        findKthFromEnd ll = new findKthFromEnd(1);
        ll.append(2);
        ll.append(3);
        ll.append(4);
        ll.append(5);
        ll.append(6);
        ll.print();
        System.out.println("Output: " + ll.findKthFromEndFunction(2).value);
    }
}
