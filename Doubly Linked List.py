class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return
            
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.get_last_node()
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)

    def get_last_node(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        if self.head is None:
            node=Node(data,self.head,None)
            self.head=node

        node = Node(data, self.head,None)
        self.head.prev=None
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None,itr)

    
