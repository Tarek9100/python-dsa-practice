class Stack():
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)


    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty, nothing to remove.")
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise IndexError("Stack is empty, nothing to peek.")
        return self.stack[-1]

    def __str__(self):
        """Return a vertical string representation of the stack (top to bottom)."""
        if not self.stack:
            return "Empty Stack"
        
        nodes = ["Top"]
        for item in reversed(self.stack):
            nodes.append(str(item))
        nodes.append("Bottom")
        return "\n".join(nodes)
    