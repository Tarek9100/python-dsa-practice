class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  
        self.length = 0
        
    def __str__(self):
        """Return a vertical string representation of the stack (top to bottom)."""
        nodes = []
        current = self.top
        while current:
            nodes.append(str(current.data))
            current = current.next
        if not nodes:
            return "Empty Stack"
        return "Top\n" + "\n".join(nodes) + "\nBottom"
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top 
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("Stack is empty, nothing to remove.")
        popped_node = self.top
        self.top = self.top.next
        self.length -= 1
        return popped_node.data  

    def peek(self):
        if self.length == 0:
            raise IndexError("Stack is empty, nothing to remove.")
        return self.top.data
    