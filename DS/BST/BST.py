class Node():
    
    def __init__(self,data):
        self.data = data
        self.left= None
        self.right= None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        """
        Inserts a new node with the given data into the binary search tree.
        """
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while current:
            if data > current.data:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
                
    def lookup(self,data):
        """
        Searches for a node with the specified data in the binary search tree.

        Args:
            data: The value to search for in the tree.

        Returns:
            Node: The node containing the specified data if found, otherwise None.
        """
        if not self.root:
            None
        current = self.root
        while current:
            if data == current.data:
                return current
            if data > current.data:
                current = current.right
            else:
                current = current.left
        return None

    def remove(self,data):
        """
        Removes a node with the specified data from the binary search tree.

        Args:
            data: The value of the node to remove.
        """
        if not self.root:
            return None
        current = self.root
        parent = None
        while current and current.data !=data:
            parent = current
            if data > current.data:
                current = current.right
            else:
                current = current.left   
        if not current:
            return None
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        elif current.left is None:
            if current == self.root:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right 
        elif current.right is None:
            if current == self.root:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
            successor = current.right
            successor_parent = current
            while successor.left:
                successor_parent = successor
                successor = successor.left
            current.data = successor.data
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
                 
    def __str__(self):
        """
        Returns a string representation of the binary search tree
        by performing an in-order traversal, which outputs the nodes in sorted order.
        """
        if self.root is None:
            return "<Empty Tree>"
        
        nodes = []
        
        def in_order_traversal(node):
            if node is not None:
                in_order_traversal(node.left)
                nodes.append(str(node.data))
                in_order_traversal(node.right)
        
        in_order_traversal(self.root)
        return " ".join(nodes)
