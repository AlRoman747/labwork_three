class Stack:
    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.mins: self.mins.append(x)
        else: self.mins.append(min(x, self.mins[-1]))

    def pop(self) -> int:
        if not self.data: raise ValueError("Stack is empty")
        self.mins.pop()
        return self.data.pop()

    def peek(self) -> int:
        if not self.data: raise ValueError("Stack is empty")
        return self.data[-1]

    def min(self) -> int:
        if not self.mins: raise ValueError("Stack is empty")
        return self.mins[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __len__(self) -> int:
        return len(self.data)


s = Stack()

s.push(3)

# print(s.peek())