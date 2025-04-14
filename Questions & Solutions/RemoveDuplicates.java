// LL: Remove Duplicates ( ** Interview Question)
// Instructions
// You are given a singly linked list that contains integer values, where some
// of these values may be duplicated.

// Note: this linked list class does NOT have a tail which will make this method
// easier to implement.

// Your task is to implement a method called removeDuplicates() within the
// LinkedList class that removes all duplicate values from the list.
// Your method should not create a new list, but rather modify the existing list
// in-place, preserving the relative order of the nodes.
// You can implement the removeDuplicates() method in two different ways:
// Using a Set (HashSet) - This approach will have a time complexity of O(n),
// where n is the number of nodes in the linked list. You are allowed to use the
// provided Set data structure in your implementation.
// Without using a Set - This approach will have a time complexity of O(n^2),
// where n is the number of nodes in the linked list. You are not allowed to use
// any additional data structures for this implementation.

// Here is the method signature you need to implement:
// public void removeDuplicates() {
// Your implementation goes here
// }

// Example:
// Input:
// LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
// Output:
// LinkedList: 1 -> 2 -> 3 -> 4 -> 5

//SOLUTION

//here in this problem what we will do is we will take two pointers
//temp and front and will use the hashSet to store the visited nodes.

import java.util.HashSet;

public class RemoveDuplicates {
    private Node head;
    int length;

    class Node {
        Node next;
        int value;

        public Node(int value) {
            this.value = value;
        }
    }

    public RemoveDuplicates(int value) {
        Node newNode = new Node(value);
        head = newNode;
        length = 1;
    }

    public void append(int value) {
        Node newnNode = new Node(value);
        if (head == null) {
            head = newnNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newnNode;
        }
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

    public void RemoveDuplicatesFunction() {
        HashSet<Integer> hs = new HashSet<>();
        Node temp = head;
        Node front = head.next;
        while (front != null) {
            hs.add(temp.value);
            if (hs.contains(front.value)) {
                temp.next = front.next;
                length--;
            } else {
                temp = temp.next;
            }
            front = front.next;
        }

    }

    public static void main(String[] args) {
        RemoveDuplicates ll = new RemoveDuplicates(1);
        ll.append(2);
        ll.append(4);
        ll.append(1);
        ll.append(4);
        ll.append(6);
        ll.append(2);
        ll.print();
        ll.RemoveDuplicatesFunction();
        System.out.println("removed duplications ------------");
        ll.print();
    }
}
