class MyStack:

    def __init__(self):
        self.queue1 = []
        self.front1 = 0
        self.rear1 = 0

        self.queue2 = []
        self.front2 = 0
        self.rear2 = 0

    def push(self, x: int) -> None:
        if not self.queue2:
            self.queue1.append(x)
            self.rear1 += 1
        else:
            self.queue1 += self.queue2
            self.rear1 += len(self.queue2)
            self.queue2 = []

    def pop(self) -> int:
        for i in range(len(self.queue1) - 1):
            self.queue2.append(self.queue1[self.front1])
            self.front1 += 1
        temp = self.queue1[self.rear1 - 1]
        self.queue1 = self.queue2.copy()
        self.rear1 -= 1
        self.front1 = 0
        self.queue2 = []
        return temp

    def top(self) -> int:
        return self.queue1[self.rear1 - 1]

    def empty(self) -> bool:
        return self.queue1 == [] and self.queue2 == []


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)

param_2 = obj.pop()
print(param_2)

param_3 = obj.pop()
print(param_3)

param_4 = obj.pop()
print(param_4)

print(obj.empty())
