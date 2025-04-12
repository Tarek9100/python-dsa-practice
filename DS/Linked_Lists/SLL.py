class Node():
    
    def __init__(self,data):
        self.data = data
        self.next= None
    
class SinglyLinkedList():
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
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1   
        
    def prepend(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
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

        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node                
        self.length += 1 
    
    def remove(self, index):
        if self.head is None:
            raise IndexError("List is empty, nothing to remove.")
            
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return
        
        if index < 0 or index >= self.length:
            raise IndexError(f"Index {index} is out of range. The list has only {self.length} elements.")
        
        current = self.head
        for _ in range(index - 1):
            current = current.next  
        target_node = current.next  
        current.next = target_node.next  
        
        if target_node == self.tail:
            self.tail = current
        self.length -= 1
      
    def reverse(self):
        if (self.length == 1):
            return self.head
        first = self.head
        second = first.next
        while(second):
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first