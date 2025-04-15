public class DoubleLinkedList {
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

    public DoubleLinkedList(int value) {
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
            length = 1;
        } else {
            tail.next = newnNode;
            newnNode.prev = tail;
            tail = newnNode;
        }
        length++;
    }

    public void prepend(int value) {
        Node newnNode = new Node(value);
        if (length == 0) {
            head = newnNode;
            tail = newnNode;
            length = 1;
        } else {
            newnNode.next = head;
            head.prev = newnNode;
            head = newnNode;
        }
        length++;
    }

    public void removeFirst() {
        if (length == 0) {
            System.out.println("LinkedList is empty couldn't remove !");
        } else {
            Node temp = head;
            head = temp.next;
            temp.next = null;
            head.prev = null;
            length--;
        }
    }

    public void removeLast() {
        if (length == 0) {
            System.out.println("LinkedList is empty couldn't remove !");
        } else if (length == 1) {
            head = null;
            tail = null;
            length = 0;
        } else {
            Node temp = tail;
            tail = tail.prev;
            tail.next = null;
            temp.prev = null;
            length--;
        }
    }

    public void removeAtIndex(int index) {
        if (index < 0 || index > length) {
            System.out.println("Index out of bound !");
        } else if (index == 1) {
            removeFirst();
            length--;
        } else if (index == length) {
            removeLast();
            length--;
        } else {
            Node temp = head;
            for (int i = 0; i < index; i++) {
                temp = temp.next;
            }
            Node previous = temp.prev;
            previous.next = temp.next;
            temp.next.prev = previous;
            length--;
        }
    }

    public Node getAtIndex(int index) {
        if (index < 0 || index > length)
            return null;
        Node temp = head;
        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp;
    }

    public void setAtIndex(int index, int value) {
        if (index < 0 || index > length) {
            System.out.println("Index out of bound !");
        } else {
            Node temp = head;
            for (int i = 0; i < index; i++) {
                temp = temp.next;
            }
            temp.value = value;
        }
    }

    public void insertAtIndex(int index, int value) {
        if (index < 0 || index > length) {
            System.out.println("Index out of bound !");
        } else {
            Node newNode = new Node(value);
            Node temp = head;
            for (int i = 0; i < index; i++) {
                temp = temp.next;
            }
            Node previous = temp.prev;
            previous.next = newNode;
            newNode.next = temp;
            temp.prev = newNode;
            newNode.prev = previous;
            length++;
        }
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

    public static void main(String[] args) {
        DoubleLinkedList dll = new DoubleLinkedList(1);
        dll.append(2);
        dll.prepend(0);
        dll.prepend(-1);
        dll.print();
        dll.removeAtIndex(2);
        dll.print();
    }
}
