class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        x = self.stack[-1]
        self.stack.pop()
        return x

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return False if len(self.stack) else True
    # def print(self):
    #     for i in self.stack:
    #         print(i)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.push(2)
# param_3 = obj.top()
# param_2 = obj.pop()
# param_3 = obj.top()
# obj.print()