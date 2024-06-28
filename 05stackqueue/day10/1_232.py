class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        if not self.stack_out:
            self.stack_in.append(x)
            return
        else:
            while self.stack_out:
                self.stack_in.append(self.stack_out.pop())
            self.stack_in.append(x)
            return

    def pop(self) -> int:
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        if not self.stack_in and not self.stack_out:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
print("param_2 = obj.pop(): ", param_2)
obj.push(5)

param_2 = obj.pop()
print("param_2 = obj.pop(): ", param_2)

param_2 = obj.pop()
print("param_2 = obj.pop(): ", param_2)

param_2 = obj.pop()
print("param_2 = obj.pop(): ", param_2)

param_2 = obj.pop()
print("param_2 = obj.pop(): ", param_2)