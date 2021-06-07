# doubly - linked list implementation

class Node:

    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_Tail(self,data):

        new_node = Node(data)
        
        #when list is empty 
        if self.head is None:
            self.head = new_node
            self.tail = new_node


        #there is atleast one item in the data strcuture

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):

        currNode = self.head

        while currNode is not None:
            print("%d"% currNode.data)
            currNode = currNode.next

    def traverse_backward(self):

        currNode = self.tail

        while currNode is not None:
            print("%d"% currNode.data)
            currNode = currNode.prev    

dll = DoublyLinkedList()

dll.insert_at_Tail(1)
dll.insert_at_Tail(2)
dll.insert_at_Tail(3)
dll.insert_at_Tail(4)
dll.insert_at_Tail(5)

dll.traverse_backward()
print("==================")
dll.traverse_forward()