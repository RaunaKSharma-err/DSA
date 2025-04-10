import org.w3c.dom.Node;

class linkedlist {
    private Node head;
    private Node tail;
    private int length;

    class Node {
        Node next;
        int value;

        public Node(int value) {
            this.value = value;
        }
    }

    public linkedlist(int value) {
        Node newNode = new Node(value);
        head = newNode;
        tail = newNode;
        length = 1;
    }

    public void print() {
        Node temp = head;
        while (temp != null) {
            System.out.println("");
            System.out.println("value: " + temp.value);
            temp = temp.next;
        }
    }

    public void printLength() {
        System.out.println("length: " + length);
    }

    public void append(int value) {
        Node newnNode = new Node(value);
        if (length == 0) {
            head = newnNode;
            tail = newnNode;
        } else {
            tail.next = newnNode;
            tail = newnNode;
        }
        length++;
    }

    public void prepend(int value) {
        Node newnNode = new Node(value);
        if (length == 0) {
            head = newnNode;
            tail = newnNode;
        } else {
            newnNode.next = head;
            head = newnNode;
        }
        length++;
    }

    public void RemoveLast() {
        if (length == 0) {
            System.out.println("LinkedList is empty !");
        } else {
            Node temp = head;
            Node pre = head;
            while (temp.next != null) {
                pre = temp;
                temp = temp.next;
            }
            tail = pre;
            tail.next = null;
            length--;
        }
    }

    public void getValueAtIndex(int index) {
        if (length == 0) {
            System.out.println("LinkedList is empty !");
        } else {
            int i = 0;
            Node temp = head;
            while (i < index) {
                temp = temp.next;
                i++;
            }
            System.out.println("Value at index " + index + " is :" + temp.value);
        }
    }

    public void RemoveFirst() {
        if (length == 0) {
            System.out.println("LinkedList is empty !");
        } else {
            head = head.next;
            length--;
        }
    }

    public static void main(String[] args) {
        linkedlist obj = new linkedlist(4);
        obj.append(10);
        obj.append(20);
        obj.append(30);
        obj.print();
        obj.getValueAtIndex(3);
    }
}