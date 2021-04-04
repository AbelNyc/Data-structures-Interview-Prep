class Node:

    def __init__(self,data,parent):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self,data,node):
        #left subtree 
        if data < node.data:
            if node.left:
                self.insert_node(data,node.left)
            else:
                node.left = Node(data,node)
        #right subtree    
        else:
            if node.right:
                self.insert_node(data,node.right)
            else:
                node.right = Node(data,node)

    #get min value in a tree
    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.right:
            return self.get_max(node.right)

        return node.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self,node):
        print
        if node.left:
            return self.get_min(node.left)
        
        return node.data
    
        
    def traverse(self):
        if self.root is not None:
            self.in_order_trasversal(self.root)
    
    def in_order_trasversal(self, node):
        if node.left:
            return self.in_order_trasversal(node.left)

        print(node.data)
        
        if node.right:
            self.in_order_trasversal(node.right)



 


bst = BinarySearchTree()
bst.insert(5)
bst.insert(6)
bst.insert(7)
bst.insert(3)
bst.insert(22)
bst.insert(4)


bst.traverse()

print("Maximum node in a BST Tree :",bst.get_max_value())
print("Minimum node in a BST Tree :",bst.get_min_value())


