class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size():
            return self.items.pop()
        else:
            return "The stack is empty"

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
