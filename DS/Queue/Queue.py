class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def peek(self):
        if self.length == 0:
            raise IndexError("Queue is empty, nothing to remove.")
        return self.first.data
    def enqueue(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.first = self.last = new_node
            self.length = 1
            return
        self.last.next = new_node
        self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            raise IndexError("Queue is empty, nothing to remove.")
        if self.length == 1:
            popped_node = self.last
            self.last = self.first = None
            self.length = 0 
            return popped_node.data
        popped_node = self.first
        self.first = self.first.next
        self.length -= 1
        return popped_node.data
    
    def __str__(self):
        """Return a string representation of the queue."""
        nodes = []
        current = self.first 
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "Front -> " + " -> ".join(nodes) + " -> Rear" if nodes else "Empty Queue"