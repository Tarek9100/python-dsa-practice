class Queue_of_stacks:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    
    def peek(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())  
        if not self.output_stack:
            raise IndexError("Queue is empty, nothing to peek.")
        return self.output_stack[-1]
    
    def enqueue(self,value):
        self.input_stack.append(value)
        
    def dequeue(self):
        value = self.peek()
        self.output_stack.pop()
        return value
    def __str__(self):

        temp_input = self.input_stack.copy()
        temp_output = self.output_stack.copy()
    
        output_elements = temp_output[::-1]
        combined = output_elements + temp_input
        if not combined:
            return "Empty Queue"
        return "Queue: " + " -> ".join(str(item) for item in combined)
