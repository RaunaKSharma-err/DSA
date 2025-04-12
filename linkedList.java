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

    public linkedlist.Node get(int index) {
        if (length == 0) {
            System.out.println("LinkedList is empty !");
        }
        Node temp = head;
        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp;
    }

    public void setValueAtIndex(int index, int value) {
        if (length == 0) {
            System.out.println("LinkedList is empty !");
        } else {
            int i = 0;
            Node temp = head;
            while (i < index) {
                temp = temp.next;
                i++;
            }
            temp.value = value;
            System.out.println("setted Value:" + temp.value + " at index " + index);
        }
    }

    public boolean insertValueAtIndex(int index, int value) {
        if (index < 0 || index > length) {
            System.out.println("couldn't insert at the index: " + index);
            return false;
        }
        if (index == 0) {
            prepend(value);
            return true;
        }
        if (index == length) {
            append(value);
            return true;
        }
        Node temp = get(index - 1);
        Node newnNode = new Node(value);
        newnNode.next = temp.next;
        temp.next = newnNode;
        length++;
        return true;
    }

    public boolean removeValueAtIndex(int index) {
        if (index < 0 || index > length) {
            System.out.println("couldn't remove the value at the index: " + index);
            return false;
        }
        if (index == 0) {
            RemoveFirst();
            return true;
        }
        if (index == length) {
            RemoveLast();
            return true;
        }
        Node presentNode = get(index);
        Node previousNode = get(index - 1);
        previousNode.next = presentNode.next;
        length--;
        return true;
    }

    public void RemoveFirst() {
        if (length == 0) {
            System.out.println("LinkedList is empty !");
        } else {
            head = head.next;
            length--;
        }
    }

    public void reverse() {
        if (length == 0) {
            System.out.println("LinkedList is empty !");
        } else {
            Node temp = head;
            head = tail;
            tail = temp;
            Node before = null;
            Node after = temp.next;
            for (int i = 0; i < length; i++) {
                after = temp.next;
                temp.next = before;
                before = temp;
                temp = after;
            }
        }
    }

    public static void main(String[] args) {
        linkedlist obj = new linkedlist(4);
        obj.append(10);
        obj.append(20);
        obj.append(30);
        obj.print();
        obj.reverse();
        obj.print();
    }
}