class Node():
    
    def __init__(self,data):
        self.data = data
        self.next= None
        self.previous= None
    
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        """Return a string representation of the linked list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) if nodes else "Empty List"       
    
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1   
        
    def prepend(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1           

    def insert(self,index,data):
        new_node = Node(data)
        
        if index == 0:
            self.prepend(data)
            return
        if index >= self.length:
            self.append(data)
            return
        
        if index <= self.length/2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - index - 1):
                current = current.previous            
        new_node.previous = current.previous
        new_node.next = current
        if current.previous:
            current.previous.next= new_node     
        current.previous= new_node              
        self.length += 1 
    
    def remove(self, index):
        if self.head is None:
            raise IndexError("List is empty, nothing to remove.")
            
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.previous = None
            self.length -= 1
            return
        
        if index < 0 or index >= self.length:
            raise IndexError(f"Index {index} is out of range. The list has only {self.length} elements.")
        
        if index <= self.length/2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - index - 1):
                current = current.previous    
        current.previous.next = current.next
        if current.next:
            current.next.previous = current.previous
        else: 
            self.tail = current.previous
        self.length -= 1
        
