function LinkedList() {
    let length = 0;
    let head = null;

    // Create nodes
    let Node = function(val) {
        this.val = val;
        this.next = null;
    }

    this.size = function() {
        return length;
    }

    this.head = function() {
        return head;
    }

    this.add = function(val) {
        // create new node with value
        let node = new Node(val);
        if(head === null) {
            head = node;
        } else {
            let currentNode = head;
            // Add it to the end by looping until end reached
            while(currentNode.next) {
                currentNode = currentNode.next;
            }
            currentNode.next = node;
        }

        length++;
    }
}

let exLinkedList = new LinkedList();
exLinkedList.add(1);
exLinkedList.add(2);