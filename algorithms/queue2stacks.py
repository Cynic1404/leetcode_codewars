class Queue2Stacks:

    def __init__(self):

        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return self.stack1 == []

    def enqueue(self, element):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(element)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        # FILL OUT CODE HERE
        return element

    def dequeue(self):
        return self.stack1.pop()
