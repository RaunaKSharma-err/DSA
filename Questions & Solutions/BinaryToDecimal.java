// LL: Binary to Decimal ( ** Interview Question)

// Instructions
// Objective:
// You have a linked list where each node represents a binary digit (0 or 1). The goal of the binaryToDecimal function is to convert this binary number, represented by the linked list, into its decimal equivalent.

// Function Signature:
// public int binaryToDecimal()

// How Binary to Decimal Conversion Works:
// In binary-to-decimal conversion, each position of a binary number corresponds to a specific power of 2, starting from the rightmost digit.
// The rightmost digit is multiplied by 2^0 (which equals 1).
// The next digit to the left is multiplied by 2^1 (which equals 2).
// The digit after that is multiplied by 2^2 (which equals 4). ... and so on.

// To find the decimal representation:
// Multiply each binary digit by its corresponding power of 2 value.
// Sum up all these products.
// Example Execution with Binary 101:
// Start with num = 0.
// Process 1 (from the head of the linked list): num = 0 * 2 + 1 = 1
// Process 0: num = 1 * 2 + 0 = 2
// Process 1: num = 2 * 2 + 1 = 5
// Return num, which is 5.

// Steps Involved in the Function:
// 1. A variable num is initialized to 0, which will store our computed decimal number.
// 2. Starting from the head of the linked list (the leftmost binary digit), iterate through each node until the end.
// 3. For every node, double the current value of num (this is analogous to shifting in binary representation). Then, add the binary digit of the current node.
// 4. Move to the next node and repeat until you've visited all nodes.
// 5. Return the value in num, which now represents the decimal value of the binary number in the linked list.

//SOLUTION

public class BinaryToDecimal {
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

    public BinaryToDecimal(int value) {
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
        for (int i = 0; i < length; i++) {
            System.out.println("");
            System.out.println(temp.value);
            temp = temp.next;
        }
    }

    public int BinaryToDecimalFunction() {
        int num = 0;
        Node temp = head;
        while (temp != null) {
            num = (num * 2) + temp.value;
            temp = temp.next;
        }
        return num;
    }

    public static void main(String[] args) {
        BinaryToDecimal ll = new BinaryToDecimal(1);
        ll.append(0);
        ll.append(1);
        ll.append(1);
        ll.append(1);
        ll.print();
        int result = ll.BinaryToDecimalFunction();
        System.out.println(result);
    }
}